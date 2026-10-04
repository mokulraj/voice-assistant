from app.commands.basic_commands import BasicCommands
from app.commands.web_commands import WebCommands
from app.voice.listener import Listener
from app.voice.speaker import Speaker


class VoiceAssistant:
    """Main controller for the voice assistant."""

    def __init__(self):
        self.listener = Listener()
        self.speaker = Speaker()

        self.basic_commands = BasicCommands()
        self.web_commands = WebCommands()

        self.running = True

    def process_command(self, text: str) -> str:
        """
        Process recognized user speech.

        Args:
            text: Recognized speech.

        Returns:
            Assistant response.
        """

        if not text:
            return (
                "Sorry, I didn't hear anything. "
                "Please try again."
            )

        response = self.basic_commands.handle(text)

        if response:
            return response

        response = self.web_commands.handle(text)

        if response:
            return response

        return (
            "Sorry, I don't understand that command yet. "
            "Please try again."
        )

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

                response = self.process_command(text)

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