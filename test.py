from rag_logic import RAGSystem

PDF_PATH = "data/Nghi_dinh_168_2024.pdf"


def main():

    print("Đang khởi tạo hệ thống...")

    rag = RAGSystem()

    print("Đang tạo Vector Database...")

    vector_db = rag.create_vector_db(PDF_PATH)

    qa_chain = rag.get_qa_chain(vector_db)

    questions = [
        "Mức phạt nồng độ cồn xe máy cao nhất là bao nhiêu?",
        "Lỗi không đội mũ bảo hiểm bị phạt như thế nào?",
        "Xe máy vượt đèn đỏ bị phạt bao nhiêu?"
    ]

    for question in questions:

        print("\n" + "=" * 60)
        print("CÂU HỎI:")
        print(question)

        result = qa_chain(question)

        print("\nTRẢ LỜI:")
        print(result["answer"])


if __name__ == "__main__":
    main()