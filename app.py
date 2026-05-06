from rag_logic import RAGSystem
import os

API_KEY = "AIzaSyBKycL-Xzsyaeu431so8F-yNXop4Bf7wQA"
PDF_PATH = "data/Nghi_dinh_168_2024.pdf" 

def run_test():
    try:
        rag = RAGSystem(API_KEY)
        vector_db = rag.create_vector_db(PDF_PATH)
        qa_chain = rag.get_qa_chain(vector_db)
        
        query = "Mức phạt nồng độ cồn xe máy cao nhất?"
        # Sử dụng 'input' làm key truyền vào
        result = qa_chain.invoke({"input": query})
        
        print(f"\n--- KẾT QUẢ TEST ---")
        print(f"Câu hỏi: {query}")
        print(f"Trả lời: {result['answer']}") # Lấy từ key 'answer'
        
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    run_test()