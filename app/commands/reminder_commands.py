import re
import threading


class ReminderCommands:
    """Handles timed reminders."""

    def __init__(self, speaker):
        self.speaker = speaker

    def set_reminder(self, text: str) -> str:
        """
        Create a reminder from a natural-language command.

        Examples:
            remind me in 10 seconds
            remind me in 1 minute
            set a timer for 30 seconds
        """
        match = re.search(
            r"(?:remind me in|set a timer for)\s+(\d+)\s+"
            r"(second|seconds|minute|minutes|hour|hours)",
            text.lower().strip()
        )

        if not match:
            return (
                "Please tell me a duration, "
                "like remind me in 10 seconds."
            )

        amount = int(match.group(1))
        unit = match.group(2)

        seconds = self._convert_to_seconds(amount, unit)

        timer = threading.Timer(
            seconds,
            self._trigger_reminder
        )
        timer.daemon = True
        timer.start()

        response_unit = self._format_unit(amount, unit)

        return (
            f"Okay, I will remind you in "
            f"{amount} {response_unit}."
        )

    def _convert_to_seconds(self, amount: int, unit: str) -> int:
        if "second" in unit:
            return amount

        if "minute" in unit:
            return amount * 60

        if "hour" in unit:
            return amount * 60 * 60

        return amount

    def _format_unit(self, amount: int, unit: str) -> str:
        """Return the correct singular/plural unit."""
        base_unit = unit.rstrip("s")

        if amount == 1:
            return base_unit

        return f"{base_unit}s"

    def _trigger_reminder(self):
        if self.speaker:
            self.speaker.speak(
                "Reminder! Your timer is finished."
            )