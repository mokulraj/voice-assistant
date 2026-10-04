import json
import re
from pathlib import Path


class IntentClassifier:
    """Classifies user sentences into assistant intents."""

    def __init__(self):
        self.intents = self._load_intents()

    def _load_intents(self) -> dict:
        """Load intent examples from the JSON configuration."""

        project_root = Path(__file__).resolve().parents[2]

        intents_file = (
            project_root
            / "app"
            / "data"
            / "intents.json"
        )

        with intents_file.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    def classify(self, text: str) -> str | None:
        """
        Classify a sentence into an intent.

        Args:
            text: User's spoken sentence.

        Returns:
            Intent name or None if no intent matches.
        """

        normalized_text = self._normalize(text)

        if not normalized_text:
            return None

        best_intent = None
        best_score = 0

        for intent_name, intent_data in self.intents.items():

            for example in intent_data["examples"]:

                normalized_example = self._normalize(example)

                score = self._calculate_score(
                    normalized_text,
                    normalized_example
                )

                if score > best_score:
                    best_score = score
                    best_intent = intent_name

        # Don't classify weak matches.
        if best_score < 0.4:
            return None

        return best_intent

    def _normalize(self, text: str) -> str:
        """Normalize text before comparison."""

        text = text.lower().strip()

        text = re.sub(
            r"[^\w\s]",
            "",
            text
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text

    def _calculate_score(
        self,
        user_text: str,
        example_text: str
    ) -> float:
        """Calculate a simple word-overlap score."""

        user_words = set(user_text.split())
        example_words = set(example_text.split())

        if not example_words:
            return 0.0

        common_words = user_words.intersection(
            example_words
        )

        return len(common_words) / len(example_words)