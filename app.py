import streamlit as st
from chatbot import get_answer, load_pdf

# --- App Config ---
st.set_page_config(page_title="PDF Chatbot", page_icon="📄", layout="wide")

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "pdf_loaded" not in st.session_state:
    st.session_state.pdf_loaded = False

# --- Sidebar ---
st.sidebar.image(
    "logo.png",
    caption="PDF Chatbot",
    use_container_width=True
)
st.sidebar.markdown("### 📄 Upload your PDFs to start chatting")

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF file(s)", type="pdf", accept_multiple_files=True
)

# Reset button
if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.session_state.pdf_loaded = False
    st.sidebar.info("Chat has been reset. Please upload a new PDF.")

# --- Load PDFs ---
if uploaded_files and not st.session_state.pdf_loaded:
    pdf_paths = []
    for i, uploaded_file in enumerate(uploaded_files):
        pdf_path = f"uploaded_{i}.pdf"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        pdf_paths.append(pdf_path)

    try:
        load_pdf(pdf_paths)   # now supports multiple PDFs
        st.session_state.pdf_loaded = True
        st.sidebar.success("✅ PDF(s) uploaded and processed!")
    except Exception as e:
        st.sidebar.error(f"⚠️ Error loading PDF: {str(e)}")

# --- Title ---
st.markdown(
    """
    <h2 style='text-align: center; color: #1E90FF; font-family: Arial, sans-serif;'>
        📄 Chat with Your PDF
    </h2>
    """,
    unsafe_allow_html=True
)

# --- Chat Display ---
chat_container = st.container()
with chat_container:
    st.markdown("<div style='max-height: 500px; overflow-y: auto;'>", unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div style='text-align: left; background-color:#E8F0FE; padding:12px 15px; 
                border-radius:15px; margin:6px 35% 6px 5px; font-family: Arial, sans-serif;
                box-shadow: 0px 1px 3px rgba(0,0,0,0.1);'>
                👤 <b>You:</b> {msg['text']}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style='text-align: left; background-color:#DFF6DD; padding:12px 15px; 
                border-radius:15px; margin:6px 5px 6px 35%; font-family: Arial, sans-serif;
                box-shadow: 0px 1px 3px rgba(0,0,0,0.1);'>
                🤖 <b>Bot:</b> {msg['text']}
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

# --- Bottom Input Box ---
if st.session_state.pdf_loaded:
    st.markdown("<hr>", unsafe_allow_html=True)
    cols = st.columns([8, 1])
    user_input = cols[0].text_input(
        "Type your message...",
        key=f"input_box_{len(st.session_state.chat_history)}",
        label_visibility="collapsed"
    )
    send = cols[1].button("Send", use_container_width=True)

    if send and user_input:
        # Save user message
        st.session_state.chat_history.append({"role": "user", "text": user_input})

        # Typing indicator
        with st.spinner("🤖 Thinking..."):
            try:
                bot_response = get_answer(user_input)
            except Exception as e:
                bot_response = f"⚠️ Error: {str(e)}"

        # Save bot response
        st.session_state.chat_history.append({"role": "bot", "text": bot_response})

        st.rerun()
else:
    st.info("👆 Please upload at least one PDF to begin chatting.")
