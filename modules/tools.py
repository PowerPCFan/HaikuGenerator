
import modules.markov_loader as markov_loader
import modules.syllables as syllables
import modules.correct_typos as correct_typos
from markovify import NewlineText
from modules.global_vars import RESET, GREEN, GREY, config

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
            if config.spell_check:
                return make_proper_sentence(line_candidate)
            else:
                return line_candidate
    return "Error generating this line."

def make_proper_sentence(text: str) -> str:
    text = text.strip()  # strip string
    
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

def print_with_border(lines: list[str], elapsed: float) -> None:
    lines = [line.strip() for line in lines]
    
    if not lines:
        return

    leftspacing: str = " " * 5
    topspacing: str = "\n" * 2
    
    haiku_ready: str = f"Your haiku is ready!"
    elapsed_message: str = f"Elapsed: {elapsed:.1f}s"
    
    # max_len: int = max(len(line) for line in lines)
    max_len: int = max(
        len(line) for line in lines + [haiku_ready, elapsed_message]
    )
    
    padded_len: int = max_len + 4
    
    bt: str = leftspacing + "╔" + "═" * (max_len + 2) + "╗"
    bb: str = leftspacing + "╚" + "═" * (max_len + 2) + "╝"

    print(topspacing)
    print(f"{leftspacing}{GREEN}{haiku_ready.center(padded_len)}{RESET}")
    print(bt)
    for line in lines:
        print(f"{leftspacing}║ {line.center(max_len)} ║")
    print(bb)
    print(f"{leftspacing}{GREY}{elapsed_message.center(padded_len)}{RESET}")
    print(topspacing)
