# Law Chatbot Project - RAG System ⚖️🤖

## Giới thiệu (Introduction)
**Vietnamese:**
Dự án tập trung xây dựng hệ thống hỗ trợ tra cứu luật thông minh nhằm thay thế phương thức đọc văn bản PDF truyền thống. Bằng cách kết hợp mô hình **Gemini 1.5 Flash** và kỹ thuật **RAG (Retrieval-Augmented Generation)**, hệ thống cho phép truy xuất chính xác các điều luật từ cơ sở dữ liệu vector **FAISS**. Dự án giúp người dùng truy vấn luật giao thông bằng ngôn ngữ tự nhiên, đảm bảo tính xác thực và giảm thiểu hiện tượng AI trả lời sai lệch.

**English:**
This project develops an intelligent chatbot to optimize the search for complex traffic regulations. By integrating **Gemini 1.5 Flash** with **Retrieval-Augmented Generation (RAG)**, the system enables precise retrieval of legal clauses from a **FAISS** vector database. The application allows users to query traffic laws using natural language, ensuring high accuracy and eliminating AI hallucinations.

---

## Công nghệ sử dụng (Tech Stack) 🛠️
*   **Language:** Python
*   **AI Framework:** LangChain
*   **LLM:** Google Gemini API (gemini-1.5-flash)
*   **Vector Database:** FAISS
*   **UI Framework:** Streamlit
*   **PDF Processing:** PyPDF

---

## Tính năng chính (Core Features) ✨
*   **Semantic Search:** Tìm kiếm theo ngữ nghĩa thay vì chỉ khớp từ khóa đơn thuần.
*   **Contextual Awareness:** Phản hồi dựa trên nội dung thực tế từ các nghị định, thông tư (file PDF).
*   **Friendly UI:** Giao diện chatbot trực quan, dễ sử dụng cho người dùng không chuyên.

