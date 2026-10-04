import re


class EntityExtractor:
    """Extracts useful information from user commands."""

    def extract_search_query(self, text: str) -> str | None:
        """
        Extract the search query from a natural-language sentence.

        Args:
            text: User's sentence.

        Returns:
            Search query or None.
        """

        patterns = [
            r"search (?:the )?(?:web|internet) for (.+)",
            r"search for (.+)",
            r"google (.+)",
            r"look up (.+)",
            r"find information about (.+)",
            r"search online for (.+)"
        ]

        normalized_text = text.lower().strip()

        for pattern in patterns:
            match = re.search(
                pattern,
                normalized_text
            )

            if match:
                query = match.group(1).strip()

                if query:
                    return query

        return None