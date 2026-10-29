# FAQ Chatbot

## Overview
The FAQ Chatbot is a Python-based web application developed using Flask. It answers frequently asked questions about artificial intelligence, machine learning, Python, chatbots, and other related topics.

## Features
- Answers common questions using keyword matching.
- Provides suggested topics to explore.
- Includes an interactive chat interface.
- Displays a fallback response when a question is not recognized.
- Allows users to clear the conversation.
- Uses a Flask backend and a responsive web interface.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure
```text
CodeAlpha_FAQ_Chatbot/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

## Installation and Setup

1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install the dependency:

   `pip install -r requirements.txt`

5. Start the chatbot:

   `python app.py`

6. Open `http://127.0.0.1:5000` in your web browser.

## How It Works
The application receives a question from the user, checks it against predefined FAQ keywords, and returns a matching answer. If no matching topic is found, it displays a fallback response.

## Internship Project
Developed as part of the CodeAlpha internship tasks.
