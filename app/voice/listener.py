import speech_recognition as sr


class Listener:
    """Handles microphone input and converts speech to text."""

    def __init__(self):
        self.recognizer = sr.Recognizer()

        # Maximum time to wait for the user to start speaking.
        self.listen_timeout = 5

        # Maximum length of one spoken command.
        self.phrase_time_limit = 10

    def listen(self) -> str | None:
        """
        Listen to the microphone and convert speech to text.

        Returns:
            Recognized text as a lowercase string.
            None when speech cannot be processed.
        """

        try:
            with sr.Microphone() as source:
                print("Listening...")

                # Adjust for background noise.
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                try:
                    audio = self.recognizer.listen(
                        source,
                        timeout=self.listen_timeout,
                        phrase_time_limit=self.phrase_time_limit
                    )

                except sr.WaitTimeoutError:
                    print("No speech detected.")
                    return None

        except OSError as error:
            print(f"Microphone error: {error}")
            return None

        try:
            print("Recognizing...")

            text = self.recognizer.recognize_google(audio)

            text = text.strip().lower()

            if not text:
                return None

            print(f"You said: {text}")

            return text

        except sr.UnknownValueError:
            print("Speech could not be understood.")
            return None

        except sr.RequestError as error:
            print(f"Speech recognition service error: {error}")
            return None