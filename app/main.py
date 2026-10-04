from app.voice.speaker import Speaker


def main():
    speaker = Speaker()

    speaker.speak("Hello! I am your Python voice assistant.")
    speaker.speak("Module one is working successfully.")


if __name__ == "__main__":
    main()