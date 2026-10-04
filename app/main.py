from app.voice.listener import Listener


def main():
    listener = Listener()

    print("Voice Assistant - Microphone Test")
    print("----------------------------------")
    print("Say something after 'Listening...'")
    print("Press Ctrl+C to stop.")
    print()

    while True:
        text = listener.listen()

        if text:
            print(f"Python received: {text}")
            print()


if __name__ == "__main__":
    main()