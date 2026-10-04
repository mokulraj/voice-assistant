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