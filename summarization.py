from transformers import pipeline
import streamlit as st

def summarize_text(text):
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        summary = " ".join([summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]["summary_text"] for chunk in chunks])
        return summary.strip()
    except Exception as e:
        st.error(f"Error during summarization: {e}")
        return ""
