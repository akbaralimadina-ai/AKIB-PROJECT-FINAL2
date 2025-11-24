import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gemini 2.0 Flash Chatbot")

st.title("🤖 Chatbot Gemini 2.0 Flash — Simple Version")

# Load API Key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Key tidak ditemukan. Pastikan disimpan di secrets.toml saat menjalankan di Colab.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

prompt = st.text_input("Tanyakan sesuatu:")

if st.button("Kirim"):
    if prompt.strip():
        with st.spinner("Sedang menjawab..."):
            response = model.generate_content(prompt)
        st.success("Jawaban:")
        st.write(response.text)
    else:
        st.warning("Teks tidak boleh kosong.")
