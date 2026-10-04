import re
import webbrowser
from urllib.parse import quote_plus


class WebCommands:
    """Handles web and browser-related commands."""

    def handle(self, text: str) -> str | None:
        """
        Process web-related commands.

        Args:
            text: Recognized speech from the user.

        Returns:
            A response string if the command is recognized.
            None otherwise.
        """

        text = text.lower().strip()

        search_query = self._extract_search_query(text)

        if search_query:
            return self.search_web(search_query)

        return None

    def _extract_search_query(self, text: str) -> str | None:
        """Extract the search topic from a spoken command."""

        patterns = [
            r"^search (?:the )?(?:web|internet) for (.+)$",
            r"^search for (.+)$",
            r"^search (.+)$",
            r"^google (.+)$",
            r"^look up (.+)$",
            r"^find information about (.+)$",
        ]

        for pattern in patterns:
            match = re.match(pattern, text)

            if match:
                query = match.group(1).strip()

                if query:
                    return query

        return None

    def search_web(self, query: str) -> str:
        """Open a Google search for the given query."""

        encoded_query = quote_plus(query)

        url = (
            "https://www.google.com/search"
            f"?q={encoded_query}"
        )

        webbrowser.open(url)

        return f"Searching the web for {query}."