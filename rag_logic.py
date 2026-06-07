import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class RAGSystem:
    def __init__(self):

        self.llm = ChatOllama(
            model="qwen2.5:1.5b",
            temperature=0.1
        )

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

    def create_vector_db(self, pdf_path):

        if not os.path.exists(pdf_path):
            raise FileNotFoundError(
                f"Không tìm thấy file PDF: {pdf_path}"
            )

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

        vector_db = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        return vector_db

    def get_qa_chain(self, vector_db):

        retriever = vector_db.as_retriever(
            search_kwargs={"k": 5}
        )

        prompt = ChatPromptTemplate.from_template(
            """
Bạn là chuyên gia luật giao thông Việt Nam.

Chỉ được sử dụng thông tin trong tài liệu.

Nếu không tìm thấy thông tin trong tài liệu,
hãy trả lời:

"Tôi không tìm thấy thông tin này trong tài liệu."

====================
TÀI LIỆU
====================

{context}

====================
CÂU HỎI
====================

{question}
"""
        )

        def ask(question):

            docs = retriever.invoke(question)

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )

            chain = (
                prompt
                | self.llm
                | StrOutputParser()
            )

            answer = chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            return {
                "answer": answer,
                "context": docs
            }

        return ask