from app.commands.basic_commands import BasicCommands
from app.commands.command_dispatcher import CommandDispatcher
from app.commands.web_commands import WebCommands


def test_greeting():
    commands = BasicCommands()
    response = commands.greeting()
    assert response == "Hello! How can I help you?"


def test_time_command():
    commands = BasicCommands()
    response = commands.get_time()
    assert response.startswith("The current time is")


def test_date_command():
    commands = BasicCommands()
    response = commands.get_date()
    assert response.startswith("Today is")


def test_search_intent():
    dispatcher = CommandDispatcher()
    intent = dispatcher.intent_classifier.classify(
        "could you search the internet for Python decorators"
    )
    assert intent == "web_search"


def test_unknown_command():
    dispatcher = CommandDispatcher()
    response = dispatcher.dispatch("play some music for me")
    assert response == (
        "Sorry, I don't understand that command yet. "
        "Please try again."
    )


def test_web_command_empty_query():
    commands = WebCommands()
    response = commands.search_web("")
    assert response == "I need a search topic."