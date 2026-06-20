import streamlit as st
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Korean": "ko"
}

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages.")

text = st.text_area(
    "Enter Text",
    height=150
)

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

if st.button("Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed")

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )
    else:
        st.warning("Please enter text.")
        