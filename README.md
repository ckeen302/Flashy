Flashy
Flashy is an AI-powered web application that transforms lecture notes into interactive flashcards. It helps users study efficiently by automating the creation of flashcards and supports multiple question types: True/False, Multiple Choice, and Fill-in-the-Blanks.

Features
Extract text from uploaded PDF or TXT files.
Automatically summarize text using AI-powered models.
Generate flashcards in multiple formats:
True/False
Multiple Choice
Fill-in-the-Blanks
Download flashcards in JSON or plain text format for offline use.
Dynamic and visually appealing flashcard designs with flipping animations.
Technologies Used
Python
Streamlit (for the web interface)
Hugging Face Transformers (for text summarization)
PyPDF2 (for PDF text extraction)
NLTK (for text tokenization)
HTML/CSS (for UI styling)
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/Flashy.git
cd Flashy
Create and activate a virtual environment:

bash
Copy code
python -m venv flashcard_env
source flashcard_env/bin/activate   # On Windows: flashcard_env\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
streamlit run app.py
Open the application in your browser at http://localhost:8501.

How to Use
Upload a PDF or TXT file containing your lecture notes.
Select the type and number of flashcards to generate.
Review the generated flashcards and download them for offline study.
Sample File
SampleLectureNotes.pdf (Include this file in the repository)
License
This project is licensed under the MIT License - see the LICENSE file for details.
