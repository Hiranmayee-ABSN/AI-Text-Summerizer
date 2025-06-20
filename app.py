import streamlit as st
from transformers import pipeline
from deep_translator import GoogleTranslator
st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title(" AI Text Summarizer with Translation")
@st.cache_resource
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer = load_model()
text_input = st.text_area(" Paste your article or paragraph here:", height=300)
translate_option = st.checkbox(" Translate the summary?")
lang_code = ""
if translate_option:
    lang_code = st.text_input("Enter target language code (e.g., 'te' for Telugu, 'hi' for Hindi):", value="te")
if st.button(" Summarize"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            summary_text = summarizer(text_input, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            st.subheader(" Summary:")
            st.write(summary_text)
            if translate_option and lang_code:
                try:
                    translated = GoogleTranslator(source='auto', target=lang_code).translate(summary_text)
                    st.subheader(" Translated Summary:")
                    st.write(translated)
                except Exception as e:
                    st.error(f"Translation failed: {e}")
