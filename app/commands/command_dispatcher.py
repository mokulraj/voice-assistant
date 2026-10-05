from app.commands.basic_commands import BasicCommands
from app.commands.web_commands import WebCommands
from app.nlp.entity_extractor import EntityExtractor
from app.nlp.intent_classifier import IntentClassifier


class CommandDispatcher:
    """Routes natural-language commands to the correct handler."""

    def __init__(self):
        self.basic_commands = BasicCommands()
        self.web_commands = WebCommands()

        self.intent_classifier = IntentClassifier()
        self.entity_extractor = EntityExtractor()

    def dispatch(self, text: str) -> str:
        """
        Process a natural-language command.

        Args:
            text: Recognized speech from the user.

        Returns:
            Assistant response.
        """

        if not text:
            return (
                "Sorry, I didn't hear anything. "
                "Please try again."
            )

        intent = self.intent_classifier.classify(text)

        print(f"Detected intent: {intent}")

        if intent == "greeting":
            return self.basic_commands.greeting()

        if intent == "time":
            return self.basic_commands.get_time()

        if intent == "date":
            return self.basic_commands.get_date()

        if intent == "web_search":
            return self._handle_web_search(text)

        return (
            "Sorry, I don't understand that command yet. "
            "Please try again."
        )

    def _handle_web_search(self, text: str) -> str:
        """Handle a web-search intent."""

        query = self.entity_extractor.extract_search_query(text)

        if not query:
            return "What would you like me to search for?"

        return self.web_commands.search_web(query)