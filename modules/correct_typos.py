from textblob import Word
import re as regexp

contraction_map = {
    "im": "I'm",
    "i m": "I'm",
    "youre": "you're",
    "you re": "you're",
    "dont": "don't",
    "don t": "don't",
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
}


# def fix_contractions(text: str) -> str:
#     words = text.split()
#     fixed_words: list[str] = [w for w in [contraction_map.get(ww.lower(), ww) for ww in words] if w is not None]
#     return ' '.join(fixed_words)

def fix_contractions(text: str) -> str:
    # Handle multi-word contractions with regex
    for key, value in contraction_map.items():
        if ' ' in key:  # Only process multi-word keys
            # Use regex to match the exact phrase with word boundaries
            text = regexp.sub(rf'\b{regexp.escape(key)}\b', value, text, flags=regexp.IGNORECASE)

    # Handle single-word contractions
    words = text.split()
    fixed_words: list[str] = [contraction_map.get(ww.lower(), ww) for ww in words]
    return ' '.join(fixed_words)


def correct(text: str) -> str:
    return fix_contractions(Word(text).correct())  # this is reeeeeally slow (the textblob word thing)
