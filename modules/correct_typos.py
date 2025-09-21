from textblob import Word
import re as regexp
from modules.global_vars import config

contraction_map = {
    "im": "I'm",
    "i m": "I'm",
    "youre": "you're",
    "you re": "you're",
    "dont": "don't",
    "don t": "don't",
    "doesn t": "doesn't",
    "doesnt": "doesn't",
    "it not": "it's not",
    "isnt": "isn't",
    "isn t": "isn't",
    "cant": "can't",
    "can t": "can't",
    "wont": "won't",
    "won t": "won't",
    "ive": "I've",
    "i ve": "I've",
    "ill": "I'll",
    "i ll": "I'll",
    "lets": "let's",
    "let s": "let's",
    "its": "it's",
    "it s": "it's",
    "i": "I",
    "it ll": "it'll",
    "wanna": "want to",
    "wan na": "want to",
    "u": "you",
    "ur": "your",
    "ca": "can't",
    "wo": "won't",
    "wheres": "where's",
    "where s": "where's",
    "whos": "who's",
    "cos": "because",
    "youd": "you'd",
    "gotta": "have to",
    "got ta": "have to",
    "shouldnt": "shouldn't",
    "shouldn t": "shouldn't",
    "you ll": "you'll",
    "youll": "you'll",
    "idk": "I don't know",
    "kinda": "sort of",
    "idc": "I don't care",
}


def fix_contractions(text: str) -> str:
    for key, value in contraction_map.items():
        if ' ' in key:
            text = regexp.sub(
                pattern=rf'\b{regexp.escape(key)}\b',
                repl=value,
                string=text,
                flags=regexp.IGNORECASE
            )

    # Handle single-word contractions
    words = text.split()
    fixed_words: list[str] = [contraction_map.get(ww.lower(), ww) for ww in words]
    return ' '.join(fixed_words)


def correct(text: str) -> str:
    if config.advanced_spell_check:
        return fix_contractions(Word(text).correct())
    else:
        return fix_contractions(text)
