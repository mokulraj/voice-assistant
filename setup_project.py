from pathlib import Path


PROJECT_STRUCTURE = {
    "app": [
        "__init__.py",
        "main.py",
    ],
    "app/config": [
        "__init__.py",
        "settings.py",
    ],
    "app/core": [
        "__init__.py",
        "assistant.py",
        "logger.py",
    ],
    "app/voice": [
        "__init__.py",
        "listener.py",
        "speaker.py",
    ],
    "app/commands": [
        "__init__.py",
        "basic_commands.py",
        "web_commands.py",
        "reminder_commands.py",
        "custom_commands.py",
    ],
    "app/nlp": [
        "__init__.py",
        "intent_classifier.py",
        "entity_extractor.py",
    ],
    "app/services": [
        "__init__.py",
        "weather_service.py",
        "email_service.py",
        "knowledge_service.py",
    ],
    "app/data": [
        "commands.json",
        "intents.json",
    ],
    "tests": [
        "__init__.py",
        "test_speaker.py",
        "test_listener.py",
        "test_commands.py",
        "test_nlp.py",
    ],
}


ROOT_FILES = [
    ".env",
    ".env.example",
    ".gitignore",
    "README.md",
    "requirements.txt",
]


def create_project_structure():
    root = Path.cwd()

    print("Creating Voice Assistant project structure...")
    print()

    # Create directories and files
    for directory, files in PROJECT_STRUCTURE.items():
        directory_path = root / directory
        directory_path.mkdir(parents=True, exist_ok=True)

        for filename in files:
            file_path = directory_path / filename

            if not file_path.exists():
                file_path.touch()
                print(f"Created: {file_path}")

    # Create root files
    for filename in ROOT_FILES:
        file_path = root / filename

        if not file_path.exists():
            file_path.touch()
            print(f"Created: {file_path}")

    print()
    print("Project structure created successfully!")
    print()
    print("Next step:")
    print("Install the required Python packages and start Module 1.")


if __name__ == "__main__":
    create_project_structure()