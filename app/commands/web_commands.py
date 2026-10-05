import webbrowser
from urllib.parse import quote_plus


class WebCommands:
    """Handles web-related commands."""

    def search_web(self, query: str) -> str:
        """
        Open a Google search for the given query.

        Args:
            query: Search topic.

        Returns:
            Spoken response.
        """

        query = query.strip()

        if not query:
            return "I need a search topic."

        encoded_query = quote_plus(query)

        url = (
            "https://www.google.com/search"
            f"?q={encoded_query}"
        )

        webbrowser.open(url)

        return f"Searching the web for {query}."