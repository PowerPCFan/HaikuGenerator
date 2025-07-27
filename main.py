import modules.markov_loader as markov_loader
import modules.syllables as syllables

MARKOV_MODEL = markov_loader.get_markov_model()

ANSI = "\033["
GREEN = ANSI + "32m"
RESET = ANSI + "0m"

def make_proper_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]  # Capitalize the first letter
    
    if not text.endswith('.'):
        text += '.'  # Add period to the end if there isn't already one
    
    return text  # Return proper sentence


def print_with_border(lines: list[str]) -> None:
    lines = [line.strip() for line in lines]
    
    if not lines:
        return

    leftspacing: str = " " * 5
    max_len = max(len(line) for line in lines)
    bt = leftspacing + "╔" + "═" * (max_len + 2) + "╗"
    bb = leftspacing + "╚" + "═" * (max_len + 2) + "╝"

    print(f"\n\n{leftspacing}{GREEN}{'  Your haiku is ready!'.center(max_len)}{RESET}")
    print(bt)
    for line in lines:
        print(f"{leftspacing}║ {line.center(max_len)} ║")
    print(bb + "\n\n")

def generate_line(syllable_count):
    for i in range(100):
        sentence = MARKOV_MODEL.make_sentence(max_words=syllable_count*3)
        if not sentence:
            continue
        words = sentence.split()
        while words and syllables.get_line_syllables(" ".join(words)) > syllable_count:
            words.pop()
        line_candidate = " ".join(words)
        if syllables.get_line_syllables(line_candidate) == syllable_count:
            return make_proper_sentence(line_candidate)
    return "Error generating this line."
    
if __name__ == "__main__":
    line1 = generate_line(syllable_count=5)
    line2 = generate_line(syllable_count=7)
    line3 = generate_line(syllable_count=5)

    print_with_border([line1, line2, line3])
