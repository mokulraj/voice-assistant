# Python Voice Assistant

A Python-based voice assistant that listens to spoken commands,
processes them, and responds using text-to-speech.

## Current Features

- Voice input through microphone
- Speech recognition
- Text-to-speech responses
- Greeting command
- Current time command
- Current date command
- Web search command
- Graceful handling of unrecognized speech
- Graceful microphone timeout handling

## Tech Stack

- Python
- SpeechRecognition
- PyAudio
- pyttsx3
- datetime
- webbrowser

## Project Structure

```text
voice-assistant/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── assistant.py
│   │
│   ├── voice/
│   │   ├── listener.py
│   │   └── speaker.py
│   │
│   ├── commands/
│   │   ├── basic_commands.py
│   │   ├── web_commands.py
│   │   ├── reminder_commands.py
│   │   └── custom_commands.py
│   │
│   ├── nlp/
│   │   ├── intent_classifier.py
│   │   └── entity_extractor.py
│   │
│   └── services/
│       ├── weather_service.py
│       ├── email_service.py
│       └── knowledge_service.py
│
├── tests/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


## Running Tests

Run the automated tests with:

```bash
python -m pytest


## Natural Language Understanding

The project includes an initial NLP layer for identifying user intent
and extracting entities from natural-language commands.

Current intents:

- greeting
- time
- date
- web_search

The NLP layer currently uses a lightweight word-overlap classifier.
It is intentionally simple so that the application architecture can
be tested before introducing more advanced machine-learning models.

Future versions may use NLTK-based machine learning or transformer
models for improved intent recognition.