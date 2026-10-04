from app.commands.basic_commands import BasicCommands


def test_greeting():
    commands = BasicCommands()

    response = commands.handle("hello")

    assert response == "Hello! How can I help you?"


def test_time_command():
    commands = BasicCommands()

    response = commands.handle("what time is it")

    assert response is not None
    assert response.startswith("The current time is")


def test_date_command():
    commands = BasicCommands()

    response = commands.handle("what is today's date")

    assert response is not None
    assert response.startswith("Today is")


def test_unknown_command():
    commands = BasicCommands()

    response = commands.handle("play music")

    assert response is None
    
from app.commands.web_commands import WebCommands


def test_search_command_extracts_query():
    commands = WebCommands()

    response = commands._extract_search_query(
        "search the web for python decorators"
    )

    assert response == "python decorators"


def test_google_command_extracts_query():
    commands = WebCommands()

    response = commands._extract_search_query(
        "google python virtual environment"
    )

    assert response == "python virtual environment"


def test_non_search_command():
    commands = WebCommands()

    response = commands._extract_search_query(
        "what time is it"
    )

    assert response is None
    
    
from app.commands.command_dispatcher import CommandDispatcher


def test_dispatcher_handles_greeting():
    dispatcher = CommandDispatcher()

    response = dispatcher.dispatch("hello")

    assert response == "Hello! How can I help you?"


def test_dispatcher_handles_unknown_command():
    dispatcher = CommandDispatcher()

    response = dispatcher.dispatch("play music")

    assert response == (
        "Sorry, I don't understand that command yet. "
        "Please try again."
    )