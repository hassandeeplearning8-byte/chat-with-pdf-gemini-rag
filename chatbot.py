"""
PDF Chatbot with Google Generative AI + LangChain
-------------------------------------------------
This module handles:
- PDF loading (single or multiple files)
- Text splitting into chunks
- Embedding with Google Generative AI
- Vector store (ChromaDB) for retrieval
- Chat chain for question answering
"""

import os
from dotenv import load_dotenv
from typing import List, Union
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("⚠️ Google API Key not found. Please add it to .env file")

# Global chain (initialized later)
rag_chain = None


def load_pdf(pdf_paths: Union[str, List[str]]):
    """
    Load one or multiple PDFs, build embeddings + retriever, and initialize the RAG chain.
    """
    global rag_chain

    # Normalize to list
    if isinstance(pdf_paths, str):
        pdf_paths = [pdf_paths]

    all_docs = []
    for path in pdf_paths:
        if not os.path.exists(path):
            raise ValueError(f"⚠️ File path {path} does not exist.")
        loader = PyPDFLoader(path)
        docs = loader.load()
        all_docs.extend(docs)

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(all_docs)

    # Embeddings + VectorStore
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})

    # LLM + Prompt Template
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3, max_tokens=500)

    system_prompt = """
    You are a professional AI assistant. Use the retrieved context
    to answer user questions accurately. 
    - If unsure, say "I don't know".
    - Keep responses concise, max 3 sentences.
    \n\n
    {context}
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}")
        ]
    )

    qa_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    rag_chain = create_retrieval_chain(retriever, qa_chain)


def get_answer(query: str) -> str:
    """Get chatbot response for a user query."""
    global rag_chain
    if rag_chain is None:
        return "⚠️ No PDF loaded yet. Please upload a PDF first."
    response = rag_chain.invoke({"input": query})
    return response["answer"]
