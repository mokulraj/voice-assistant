from datetime import datetime


class BasicCommands:
    """Handles basic voice assistant commands."""

    def handle(self, text: str) -> str | None:
        """
        Process basic commands.

        Args:
            text: User's recognized speech.

        Returns:
            A response string if the command is recognized.
            None if this command handler cannot handle it.
        """

        text = text.lower().strip()

        if self._is_greeting(text):
            return self.greeting()

        if self._is_time_request(text):
            return self.get_time()

        if self._is_date_request(text):
            return self.get_date()

        return None

    def _is_greeting(self, text: str) -> bool:
        """Check whether the user is greeting the assistant."""

        greetings = [
            "hello",
            "hi",
            "hey",
            "hello assistant",
            "hi assistant",
            "hey assistant",
            "good morning",
            "good afternoon",
            "good evening",
        ]

        return any(greeting in text for greeting in greetings)

    def greeting(self) -> str:
        """Return a greeting response."""

        return "Hello! How can I help you?"

    def _is_time_request(self, text: str) -> bool:
        """Check whether the user is asking for the current time."""

        keywords = [
            "what time is it",
            "current time",
            "tell me the time",
            "what is the time",
            "time now",
        ]

        return any(keyword in text for keyword in keywords)

    def get_time(self) -> str:
        """Return the current time."""

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."

    def _is_date_request(self, text: str) -> bool:
        """Check whether the user is asking for today's date."""

        keywords = [
            "what is today's date",
            "what is the date",
            "today's date",
            "current date",
            "tell me the date",
        ]

        return any(keyword in text for keyword in keywords)

    def get_date(self) -> str:
        """Return today's date."""

        current_date = datetime.now().strftime("%A, %B %d, %Y")

        return f"Today is {current_date}."