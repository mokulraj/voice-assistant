import speech_recognition as sr


class Listener:
    """Handles microphone input and converts speech to text."""

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self) -> str:
        """
        Listen to the microphone and convert speech to text.

        Returns:
            str: The recognized speech in lowercase.
        """

        with sr.Microphone() as source:
            print("Listening...")

            # Adjust the microphone for surrounding noise.
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""

        try:
            print("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            print(f"You said: {text}")

            return text.lower()

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""

        except sr.RequestError as error:
            print(f"Speech recognition service error: {error}")
            return ""