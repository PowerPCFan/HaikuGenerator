from textblob import Word

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
    "i": "I"
}

def fix_contractions(text: str) -> str:
    words = text.split()
    fixed_words: list[str] = [w for w in [contraction_map.get(ww.lower(), ww) for ww in words] if w is not None]
    return ' '.join(fixed_words)

def correct(text: str) -> str:
    return fix_contractions(Word(text).correct())
