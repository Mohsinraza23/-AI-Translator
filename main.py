import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set Gemini key
genai.configure(api_key=api_key)

# Supported Languages
languages = [
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Vietnamese", "Hebrew", "Malay", "Czech", "Romanian", "Finnish"
]

# Streamlit UI
st.set_page_config(page_title="Translator by Mohsin", layout="centered")
st.title("🌐 AI Translator")
st.write("Created by **Mohsin Raza** – Translate your English text into various languages using Gemini AI.")

text = st.text_area("Enter English text to translate:", height=150)
lang = st.selectbox("Select target language:", languages)
btn = st.button("Translate")

if btn and text:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Translate the following text to {lang}:\n\n{text}"
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"**{response.text}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
