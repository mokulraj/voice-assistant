from app.commands.command_dispatcher import CommandDispatcher
from app.voice.listener import Listener
from app.voice.speaker import Speaker


class VoiceAssistant:
    """Main controller for the voice assistant."""

    def __init__(self):
        self.listener = Listener()
        self.speaker = Speaker()
        self.command_dispatcher = CommandDispatcher()

        self.running = True

    def run(self):
        """Start the voice assistant."""

        self.speaker.speak(
            "Hello! Voice assistant started. "
            "How can I help you?"
        )

        while self.running:

            try:
                text = self.listener.listen()

                if text is None:
                    self.speaker.speak(
                        "Sorry, I could not understand you. "
                        "Please try again."
                    )
                    continue

                response = self.command_dispatcher.dispatch(text)

                self.speaker.speak(response)

            except KeyboardInterrupt:
                self.stop()

            except Exception as error:
                print(f"Unexpected application error: {error}")

                self.speaker.speak(
                    "Something went wrong. "
                    "Please try again."
                )

    def stop(self):
        """Stop the voice assistant."""

        self.running = False

        print("\nStopping voice assistant...")

        self.speaker.speak("Goodbye!")