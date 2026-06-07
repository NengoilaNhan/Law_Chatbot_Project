import streamlit as st

from rag_logic import RAGSystem

PDF_PATH = "data/Nghi_dinh_168_2024.pdf"


@st.cache_resource
def load_system():

    rag = RAGSystem()

    vector_db = rag.create_vector_db(PDF_PATH)

    return rag.get_qa_chain(vector_db)


st.set_page_config(
    page_title="Chatbot Luật Giao Thông",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Chatbot Luật Giao Thông Việt Nam")

st.markdown(
    """
### Công nghệ sử dụng

- Ollama (Qwen3 8B)
- HuggingFace Embeddings
- FAISS
- PDF RAG
"""
)

try:

    qa_chain = load_system()

    question = st.text_area(
        label="Nhập câu hỏi",
        height=120,
        placeholder="Ví dụ: Mức phạt nồng độ cồn xe máy cao nhất là bao nhiêu?"
    )

    if st.button("Tra cứu"):

        if question.strip():

            with st.spinner("Đang xử lý..."):

                result = qa_chain(question)

            st.success("Kết quả")

            st.write(result["answer"])

except Exception as e:

    st.error(str(e))