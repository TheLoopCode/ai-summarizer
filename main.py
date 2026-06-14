import streamlit as st
import pytesseract
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("CHAT_KEY") 
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
