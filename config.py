GLOBAL_CSS = """
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(120deg, #282c34, #4a4e69); /* Dark gradient background */
        color: #f5f5f5;
        margin: 0;
        padding: 0;
    }

    .header {
        text-align: center;
        background-color: #4a4e69;
        padding: 20px 10px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        margin-bottom: 30px;
    }

    .header h1 {
        font-size: 36px;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 0;
    }

    .header p {
        font-size: 18px;
        color: #b3b3b3;
        margin-top: 5px;
    }

    .flashcard-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(600px, 1fr)); /* Adjusted for larger cards */
        gap: 20px;
        justify-items: center;
        margin-top: 20px;
        padding: 10px;
    }

    .flashcard {
        width: 600px; /* Increased width */
        height: 450px; /* Increased height */
        perspective: 1000px;
        margin: 10px;
        cursor: pointer;
    }

    .flashcard-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }

    .flashcard:hover .flashcard-inner {
        transform: rotateY(180deg);
    }

    .flashcard-front, .flashcard-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        padding: 30px;
        font-size: 18px;
        font-weight: bold;
        line-height: 1.4;
        overflow: auto; /* Add scrolling for large content */
        word-wrap: break-word;
        white-space: normal;
        text-align: left; /* Align text to the left for better readability */
    }

    .flashcard-front {
        background: linear-gradient(135deg, #6a8caf, #89c2d9); /* Cool blue gradient */
        color: #fff;
    }

    .flashcard-back {
        background: linear-gradient(135deg, #ffecd2, #fcb69f); /* Soft peach gradient */
        color: #1a1a1a;
        transform: rotateY(180deg);
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #ffffff;
        background-color: rgba(0, 0, 0, 0.8);
        padding: 10px;
        border-radius: 5px;
    }
    </style>
"""


HEADER_HTML = """
    <div class="header">
        <h1>AI-Powered Flashcard Generator</h1>
        <p>Turn your notes into interactive flashcards in seconds!</p>
    </div>
"""
