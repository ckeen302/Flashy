import random
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def extract_key_sentences(text, num_sentences=5):
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    return sentences[:num_sentences]

def generate_flashcards(sentences, num_requested, question_types):
    flashcards = []
    used_questions = set()

    for sentence in sentences:
        for question_type in question_types:
            if question_type == "True/False":
                is_false = random.choice([True, False])
                if is_false:
                    altered_sentence = sentence.replace("AI", "Data Science") if "AI" in sentence else sentence + " (Incorrect Detail)"
                    question = f"True or False: {altered_sentence}"
                    answer = f"False\n\nCorrect Answer:\n{sentence}"
                else:
                    question = f"True or False: {sentence}"
                    answer = "True"
            elif question_type == "Multiple-Choice":
                # Use the full statement as part of the question
                question = f"What is the main focus of this statement?\n\n{sentence}"

                # Dynamically extract the main focus (e.g., proper nouns, key terms)
                tokens = word_tokenize(sentence)
                pos_tags = pos_tag(tokens)
                main_focus = [word for word, pos in pos_tags if pos.startswith("NN") or pos.startswith("JJ")]
                correct_answer = main_focus[0] if main_focus else "Artificial Intelligence"  # Fallback

                # Generate plausible distractors
                distractors = ["Data Science", "Machine Learning", "Cybersecurity", "Cloud Computing"]
                if correct_answer in distractors:
                    distractors.remove(correct_answer)
                random.shuffle(distractors)

                # Add correct answer to distractors and shuffle again
                options = distractors[:3] + [correct_answer]
                random.shuffle(options)

                formatted_options = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(options)])
                full_question = f"{question}\n\nOptions:\n{formatted_options}"
                answer = correct_answer
            elif question_type == "Fill-in-the-Blanks":
                # Tokenize and identify important words (nouns, verbs, adjectives)
                tokens = word_tokenize(sentence)
                pos_tags = pos_tag(tokens)

                # Select only nouns, verbs, or adjectives as potential blanks
                important_words = [word for word, pos in pos_tags if pos.startswith("NN") or pos.startswith("VB") or pos.startswith("JJ")]

                if important_words:
                    word_to_replace = random.choice(important_words)
                    replaced_sentence = sentence.replace(word_to_replace, "____", 1)
                    question = f"{replaced_sentence}"
                    answer = f"The missing word is: {word_to_replace}"
                else:
                    question = sentence
                    answer = f"The missing word is: {sentence}"
            else:
                question = f"What does this statement mean: {sentence}?"
                answer = sentence

            if question in used_questions:
                continue
            used_questions.add(question)
            flashcards.append({"question": full_question, "answer": answer})

            if len(flashcards) >= num_requested:
                break

        if len(flashcards) >= num_requested:
            break

    return flashcards

def render_flashcards(flashcards):
    import streamlit as st
    st.markdown('<div class="flashcard-container">', unsafe_allow_html=True)
    for card in flashcards:
        st.markdown(f"""
            <div class="flashcard">
                <div class="flashcard-inner">
                    <div class="flashcard-front">
                        <h4 style="white-space: normal; word-wrap: break-word; line-height: 1.8;">{card['question']}</h4>
                    </div>
                    <div class="flashcard-back">
                        <p style="white-space: normal; word-wrap: break-word; line-height: 1.8;">{card['answer']}</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
