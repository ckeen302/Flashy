import streamlit as st
from text_processing import extract_text_from_pdf, extract_text_from_txt
from summarization import summarize_text
from flashcards import extract_key_sentences, generate_flashcards, render_flashcards
import config
import nltk
import json

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# Apply global CSS and header
st.markdown(config.GLOBAL_CSS, unsafe_allow_html=True)
st.markdown(config.HEADER_HTML, unsafe_allow_html=True)

# File upload section
uploaded_file = st.file_uploader("Upload your lecture notes (.txt or .pdf)", type=["txt", "pdf"])

if uploaded_file:
    # Extract text from file
    if uploaded_file.name.endswith(".pdf"):
        extracted_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        extracted_text = extract_text_from_txt(uploaded_file)

    # Display extracted text
    st.subheader("Extracted Text")
    st.text_area("Preview of the extracted text:", extracted_text, height=200)

    # Summarize text
    if st.button("Summarize Text"):
        with st.spinner("Summarizing..."):
            st.session_state.summarized_text = summarize_text(extracted_text)

if "summarized_text" in st.session_state and st.session_state.summarized_text:
    st.subheader("Summarized Text")
    st.text_area("Preview of the summarized text:", st.session_state.summarized_text, height=200)

    # Flashcard options
    num_flashcards = st.number_input("Enter the number of flashcards to generate:", min_value=1, max_value=20, value=5)
    st.subheader("Select the type of questions to generate:")
    question_types = []
    if st.checkbox("True/False"):
        question_types.append("True/False")
    if st.checkbox("Multiple-Choice"):
        question_types.append("Multiple-Choice")
    if st.checkbox("Fill-in-the-Blanks"):
        question_types.append("Fill-in-the-Blanks")

    # Generate and render flashcards
    if st.button("Generate Flashcards"):
        sentences = extract_key_sentences(st.session_state.summarized_text, num_flashcards)
        flashcards = generate_flashcards(sentences, num_flashcards, question_types)
        render_flashcards(flashcards)

        # Allow users to download flashcards as JSON
        flashcards_data = json.dumps(flashcards, indent=4)
        st.download_button(
            label="Download Flashcards (JSON)",
            data=flashcards_data,
            file_name="flashcards.json",
            mime="application/json"
        )

        # Optionally allow download as plain text
        flashcards_text = "\n\n".join([f"Q: {card['question']}\nA: {card['answer']}" for card in flashcards])
        st.download_button(
            label="Download Flashcards (Text)",
            data=flashcards_text,
            file_name="flashcards.txt",
            mime="text/plain"
        )

# Footer
st.markdown('<div class="footer">Built with ❤️ using Streamlit | Designed by [Your Name]</div>', unsafe_allow_html=True)
