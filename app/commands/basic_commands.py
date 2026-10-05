from datetime import datetime


class BasicCommands:
    """Provides basic assistant responses."""

    def greeting(self) -> str:
        """Return a greeting response."""

        return "Hello! How can I help you?"

    def get_time(self) -> str:
        """Return the current time."""

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."

    def get_date(self) -> str:
        """Return today's date."""

        current_date = datetime.now().strftime(
            "%A, %B %d, %Y"
        )

        return f"Today is {current_date}."