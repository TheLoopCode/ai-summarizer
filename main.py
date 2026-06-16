import streamlit as st
import pytesseract
from PIL import Image
import ollama

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

st.title("AI Summarizer (Ollama)")

text = st.text_area("Paste text here")

if st.button("Summarize"):
    res = ollama.chat(
        model="llama3.1",
        messages=[{
            "role": "user",
            "content": f"Summarize this:\n\n{text}"
        }]
    )

    st.write(res["message"]["content"])

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

