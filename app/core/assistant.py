from app.commands.basic_commands import BasicCommands
from app.voice.listener import Listener
from app.voice.speaker import Speaker


class VoiceAssistant:
    """Main controller for the voice assistant."""

    def __init__(self):
        self.listener = Listener()
        self.speaker = Speaker()
        self.basic_commands = BasicCommands()

    def process_command(self, text: str) -> str:
        """
        Process recognized user speech.

        Args:
            text: Recognized speech.

        Returns:
            Assistant response.
        """

        if not text:
            return "Sorry, I didn't hear anything."

        response = self.basic_commands.handle(text)

        if response:
            return response

        return (
            "Sorry, I don't understand that command yet. "
            "Please try again."
        )

    def run(self):
        """Start the continuous voice assistant loop."""

        self.speaker.speak(
            "Hello! Voice assistant started. "
            "How can I help you?"
        )

        while True:
            try:
                text = self.listener.listen()

                if not text:
                    self.speaker.speak(
                        "Sorry, I could not understand you. "
                        "Please try again."
                    )
                    continue

                response = self.process_command(text)

                self.speaker.speak(response)

            except KeyboardInterrupt:
                print("\nStopping voice assistant...")

                self.speaker.speak(
                    "Goodbye!"
                )

                break