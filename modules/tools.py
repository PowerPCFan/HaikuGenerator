
import modules.markov_loader as markov_loader
import modules.syllables as syllables
import modules.correct_typos as correct_typos
from modules.global_vars import config
from typing import Any

MARKOV_MODEL = markov_loader.get_markov_model()


def get_user_friendly_type(value: Any) -> str:
    value_type = type(value).__name__

    mapping = {
        "str": "string",
        "int": "integer",
        "float": "floating-point number",
        "bool": "boolean",
        "list": "list",
        "dict": "dictionary"
    }

    return mapping.get(value_type, value_type)


def regenerate_markov_model() -> None:
    markov_loader.delete_markov_model()
    markov_loader.create_and_save_markov_model()
    global MARKOV_MODEL
    MARKOV_MODEL = markov_loader.get_markov_model()


def generate_line(syllable_count: int) -> str:
    for _ in range(config.max_generation_attempts):
        sentence: str | None = MARKOV_MODEL.make_sentence(max_words=(syllable_count * 3))
        if not sentence:
            continue

        words: list[str] = sentence.split()

        while words and syllables.get_line_syllables(" ".join(words)) > syllable_count:
            words.pop()

        if not words:
            continue

        line_candidate: str = make_proper_sentence(" ".join(words))

        # Make sure the processed line isn't empty and has the right syllable count
        if line_candidate and syllables.get_line_syllables(line_candidate) == syllable_count:
            return line_candidate
    return ''


def make_proper_sentence(text: str) -> str:
    text = text.strip()

    if not text:
        return ""

    text = correct_typos.correct(text)

    text = text[0].upper() + text[1:]  # Capitalize the first letter
    text = text.replace('  ', ' ')  # Replace double spaces with single spaces
    text = text.replace('\n', ' ')  # Replace newlines with spaces
    # removed due to issues having to do with spell check
    # text += '.' if not text.endswith('.') else ''  # Add period to the end if there isn't already one
    text = text.replace(' .', '.')  # Remove space before period
    text = text.replace(' ,', ',')  # Remove space before comma
    text = text.replace(' ;', ';')  # Remove space before semicolon
    text = text.replace(' !', '!')  # Remove space before exclamation mark
    text = text.replace(' ?', '?')  # Remove space before question mark
    text = text.replace(' :', ':')  # Remove space before colon

    return text  # Return proper sentence
