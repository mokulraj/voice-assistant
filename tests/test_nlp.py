from app.nlp.entity_extractor import EntityExtractor
from app.nlp.intent_classifier import IntentClassifier


def test_greeting_intent():
    classifier = IntentClassifier()

    result = classifier.classify(
        "hello assistant"
    )

    assert result == "greeting"


def test_time_intent():
    classifier = IntentClassifier()

    result = classifier.classify(
        "can you tell me the current time"
    )

    assert result == "time"


def test_date_intent():
    classifier = IntentClassifier()

    result = classifier.classify(
        "what is the current date"
    )

    assert result == "date"


def test_search_entity():
    extractor = EntityExtractor()

    result = extractor.extract_search_query(
        "search the web for python decorators"
    )

    assert result == "python decorators"


def test_unknown_intent():
    classifier = IntentClassifier()

    result = classifier.classify(
        "play some music for me"
    )

    assert result is None
    
    
def test_reminder_intent():
    classifier = IntentClassifier()

    result = classifier.classify(
        "remind me in 10 seconds"
    )

    assert result == "reminder"