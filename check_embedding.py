from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

emb = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004"
)

result = emb.embed_query("Xin chào")

print(len(result))