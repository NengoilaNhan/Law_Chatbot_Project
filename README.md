# Law Chatbot Project

Chatbot tra cứu văn bản pháp luật Việt Nam sử dụng RAG (Retrieval-Augmented Generation) chạy hoàn toàn local trên Windows.

## Công nghệ sử dụng

* LangChain
* Ollama
* Qwen2.5:1.5B
* HuggingFace Embeddings
* FAISS Vector Database
* Streamlit
* PyPDF

## Cấu trúc dự án

```text
Law_Chatbot_Project/
│
├── app.py
├── rag_logic.py
├── test.py
├── requirements.txt
├── README.md
│
├── data/
│   └── Nghi_dinh_168_2024.pdf
│
└── faiss_index/
```

## Yêu cầu hệ thống

### Phần mềm

* Python 3.11+
* Ollama

Tải Ollama:

https://ollama.com/download

### RAM khuyến nghị

* Tối thiểu: 8GB
* Khuyến nghị: 16GB+

## Cài đặt

### Clone dự án

```bash
git clone https://github.com/NengoilaNhan/Law_Chatbot_Project.git

cd Law_Chatbot_Project
```

### Tạo môi trường ảo

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### Cài thư viện

```bash
pip install -r requirements.txt
```

## Cài đặt mô hình Ollama

Tải model:

```bash
ollama pull qwen2.5:1.5b
```

Kiểm tra:

```bash
ollama list
```

Ví dụ:

```text
NAME            SIZE
qwen2.5:1.5b    1.0 GB
```

## Kiểm tra Ollama

Tạo file test:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

print(llm.invoke("Hãy trả lời bằng tiếng Việt").content)
```

Chạy:

```bash
python test_ollama.py
```

## Chạy kiểm thử RAG

```bash
python test.py
```

## Chạy giao diện Streamlit

```bash
streamlit run app.py
```

Sau khi chạy:

```text
http://localhost:8501
```

## Cách hoạt động

1. Đọc file PDF luật.
2. Chia văn bản thành các đoạn nhỏ.
3. Sinh embedding bằng HuggingFace.
4. Lưu vào FAISS.
5. Truy xuất các đoạn liên quan.
6. Gửi ngữ cảnh vào Qwen2.5 qua Ollama.
7. Sinh câu trả lời bằng tiếng Việt.

## Ưu điểm

* Chạy hoàn toàn local.
* Không cần OpenAI API.
* Không cần Gemini API.
* Không tốn phí token.
* Dữ liệu không gửi ra ngoài.

## Tác giả

NengoilaNhan