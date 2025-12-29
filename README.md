# 🤖 Intelligent Chat with PDF (RAG using Gemini 2.0)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)](https://python.langchain.com/)
[![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=flat&logo=googlebard&logoColor=white)](https://deepmind.google/technologies/gemini/)

> **Stop searching. Start conversing with your documents.**

---

## 📖 Overview

This capstone project solves the problem of information overload in dense PDF documents. Instead of relying on inefficient "Ctrl+F" keyword searches, this application allows users to have natural, context-aware conversations with their data.

Built using a **Retrieval-Augmented Generation (RAG)** architecture, the system ingests PDF documents, creates semantic embeddings, and uses **Google's state-of-the-art Gemini 2.0 Flash LLM** to provide accurate, grounded answers instantly. The entire experience is wrapped in a user-friendly **Streamlit** web interface.

### 📺 Demo & Architecture

---

## ✨ Key Features

* **🗣️ Natural Language Querying:** Ask questions in plain English just like you're talking to a human expert on the document.
* **⚡ Powered by Gemini 2.0 Flash:** Leverages Google's latest model for exceptionally fast reasoning and concise responses.
* **🧠 Grounded Accuracy (RAG):** Answers are generated *only* from the document context, minimizing AI hallucinations.
* **🔍 Deep Semantic Search:** Uses **ChromaDB** and Google GenAI embeddings to find relevant information based on meaning, not just matching words.
* **📂 Simple PDF Upload:** Drag-and-drop interface to process documents instantly.
* **💬 Interactive UI:** Clean chat interface built with Streamlit, showing conversation history.

---

## 🛠️ Tech Stack

| Component | Technology Used | Description |
| :--- | :--- | :--- |
| **LLM (The Brain)** | Google Gemini 2.0 Flash | High-speed generation and reasoning. |
| **Embeddings** | Google GenAI (`embedding-001`) | Converts text into vector representations. |
| **Orchestration** | LangChain | Manages the RAG pipeline, document loading, and splitting. |
| **Vector Database** | ChromaDB | Stores and retrieves semantic embeddings locally. |
| **Frontend UI** | Streamlit | Python framework for building the web app interface. |
| **Language** | Python 3.10+ | Main programming language. |

---

## 🚀 Getting Started (Local Installation)

Follow these steps to set up the project on your local machine.

### Prerequisites

* Python 3.10 or higher installed.
* A Google Cloud API Key with access to the Gemini API.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/hassandeeplearning8-byte/chat-with-pdf-gemini-rag.git](https://github.com/hassandeeplearning8-byte/chat-with-pdf-gemini-rag.git)
    cd chat-with-pdf-gemini-rag
    ```

2.  **Create a Virtual Environment (Recommended):**
    It's best practice to isolate dependencies.
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    * Create a new file named `.env` in the root directory.
    * Add your Google API key to this file:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

5.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```
    The app should automatically open in your browser at `http://localhost:8501`.

---

## 📝 Usage Guide

1.  **Upload:** On the left sidebar, click "Browse files" and select a PDF document.
2.  **Process:** Click the "Process PDF" button. Wait for the "✅ PDF processed!" message.
3.  **Ask:** Type your question in the chat input box at the bottom of the main screen and hit enter.

---

## 🔮 Future Improvements

* Add support for multiple file formats (DOCX, TXT, Markdown).
* Implement chat history persistence so conversations aren't lost on refresh.
* Add "Sources" citations, allowing the user to see exactly which document chunk the answer came from.
* Dockerize the application for easy cloud deployment.

---

## 👨‍💻 Author

**Hassan Khalid**
* Data Scientist | AI Engineer
* [LinkedIn Profile](www.linkedin.com/in/hassan-khalid-deep/)