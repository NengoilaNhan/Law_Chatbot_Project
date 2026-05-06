from rag_logic import RAGSystem
import os

API_KEY = "AIzaSyBKycL-Xzsyaeu431so8F-yNXop4Bf7wQA"
PDF_PATH = "data/Nghi_dinh_168_2024.pdf" 

def run_test():
    print("--- ĐANG KHỞI TẠO HỆ THỐNG RAG 2026 ---")
    try:
        rag = RAGSystem(API_KEY)
        if not os.path.exists(PDF_PATH):
            print(f"Lỗi: Không tìm thấy file tại {PDF_PATH}")
            return

        print("Đang nạp dữ liệu pháp luật...")
        vector_db = rag.create_vector_db(PDF_PATH)
        qa_chain = rag.get_qa_chain(vector_db)
        print("✅ Hệ thống sẵn sàng!\n")

        test_questions = ["Mức phạt nồng độ cồn xe máy cao nhất?", "Lỗi không đội mũ bảo hiểm bị phạt bao nhiêu?"]

        for query in test_questions:
            print(f"Câu hỏi: {query}")
            # Sử dụng invoke với key 'input' thay cho 'query'
            response = rag_chain.invoke({"input": "Câu hỏi của bạn ở đây"})
            print(response["answer"])

    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    run_test()