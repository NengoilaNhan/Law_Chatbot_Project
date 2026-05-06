import google.generativeai as genai

# Cấu hình API Key mới của bạn
API_KEY = "AIzaSyBKycL-Xzsyaeu431so8F-yNXop4Bf7wQA"
genai.configure(api_key=API_KEY)

def setup_model():
    try:
        # Thử dùng tên model chính thức
        # Nếu vẫn lỗi 404, bạn có thể thử 'gemini-1.5-flash-latest'
        model_name = 'gemini-1.5-flash' 
        
        model = genai.GenerativeModel(model_name)
        
        # Test thử một câu lệnh đơn giản
        response = model.generate_content("Xin chào, bạn là ai?")
        print(f"Sử dụng model: {model_name}")
        print(f"Phản hồi: {response.text}")
        
    except Exception as e:
        print(f"Lỗi: {e}")
        print("\n--- Danh sách các model bạn có quyền truy cập: ---")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")

if __name__ == "__main__":
    setup_model()