
import modules.markov_loader as markov_loader
import modules.syllables as syllables
from markovify import NewlineText
from modules.global_vars import RESET, GREEN

MARKOV_MODEL: NewlineText = markov_loader.get_markov_model()

def generate_line(syllable_count: int) -> str:
    for i in range(100):
        sentence: str | None = MARKOV_MODEL.make_sentence(max_words=syllable_count*3)
        if not sentence:
            continue
        words: list[str] = sentence.split()
        while words and syllables.get_line_syllables(" ".join(words)) > syllable_count:
            words.pop()
        line_candidate: str = " ".join(words)
        if syllables.get_line_syllables(line_candidate) == syllable_count:
            return make_proper_sentence(line_candidate)
    return "Error generating this line."

def make_proper_sentence(text: str) -> str:
    text = text.strip()  # strip string
    
    text = text[0].upper() + text[1:]  # Capitalize the first letter
    text = text.replace('  ', ' ')  # Replace double spaces with single spaces
    text = text.replace('\n', ' ')  # Replace newlines with spaces
    text += '.' if not text.endswith('.') else ''  # Add period to the end if there isn't already one
    text = text.replace(' .', '.')  # Remove space before period
    text = text.replace(' ,', ',')  # Remove space before comma
    text = text.replace(' ;', ';')  # Remove space before semicolon
    text = text.replace(' !', '!')  # Remove space before exclamation mark
    text = text.replace(' ?', '?')  # Remove space before question mark
    text = text.replace(' :', ':')  # Remove space before colon

    return text  # Return proper sentence

def print_with_border(lines: list[str]) -> None:
    lines = [line.strip() for line in lines]
    
    if not lines:
        return

    leftspacing: str = " " * 5
    max_len: int = max(len(line) for line in lines)
    bt: str = leftspacing + "╔" + "═" * (max_len + 2) + "╗"
    bb: str = leftspacing + "╚" + "═" * (max_len + 2) + "╝"

    print(f"\n\n{leftspacing}{GREEN}{'  Your haiku is ready!'.center(max_len)}{RESET}")
    print(bt)
    for line in lines:
        print(f"{leftspacing}║ {line.center(max_len)} ║")
    print(bb + "\n\n")
