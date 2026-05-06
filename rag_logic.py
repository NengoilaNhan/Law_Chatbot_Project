import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# PHẦN QUAN TRỌNG: Sửa lại các dòng gây lỗi ModuleNotFoundError
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

class RAGSystem:
    def __init__(self, api_key):
        # Thiết lập API Key cho Gemini
        os.environ["GOOGLE_API_KEY"] = api_key
        
        # Khởi tạo mô hình ngôn ngữ Gemini 1.5 Flash
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", 
            temperature=0.1
        )
        
        # Khởi tạo mô hình Embedding của Google
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    def create_vector_db(self, pdf_path):
        """Nạp file PDF và tạo cơ sở dữ liệu vector."""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"Không tìm thấy file PDF tại: {pdf_path}")
            
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        # Chia nhỏ văn bản để tra cứu chính xác (phù hợp với văn bản luật)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        
        # Lưu vào FAISS vector store
        vector_db = FAISS.from_documents(chunks, self.embeddings)
        return vector_db

    def get_qa_chain(self, vector_db):
        """Tạo chuỗi phản hồi (Chain) sử dụng kiến trúc RAG mới."""
        
        # Cấu hình Prompt để chatbot đóng vai chuyên gia luật
        system_prompt = (
            "Bạn là một trợ lý chuyên gia về luật giao thông Việt Nam. "
            "Sử dụng các đoạn ngữ cảnh (context) dưới đây để trả lời câu hỏi. "
            "Nếu không có thông tin trong ngữ cảnh, hãy nói bạn không biết, đừng tự ý bịa câu trả lời. "
            "\n\n"
            "{context}"
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        # 1. Tạo chuỗi kết hợp tài liệu (Combine Documents Chain)
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        
        # 2. Tạo chuỗi truy vấn hoàn chỉnh (Retrieval Chain)
        # Sử dụng .as_retriever() để tìm kiếm trong vector_db
        rag_chain = create_retrieval_chain(
            vector_db.as_retriever(search_kwargs={"k": 5}), 
            question_answer_chain
        )
        
        return rag_chain