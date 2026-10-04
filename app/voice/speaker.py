import pyttsx3


class Speaker:
    """Handles text-to-speech output."""

    def __init__(self):
        self.engine = pyttsx3.init()

        # Speech speed
        self.engine.setProperty("rate", 170)

        # Volume: 0.0 to 1.0
        self.engine.setProperty("volume", 1.0)

    def speak(self, text: str) -> None:
        """Speak the provided text."""

        if not text:
            return

        print(f"Assistant: {text}")

        self.engine.say(text)
        self.engine.runAndWait()