import modules.tools as tools
from modules.global_vars import RED, RESET

if __name__ == "__main__":
    try:
        line1: str = tools.generate_line(syllable_count=5)
        line2: str = tools.generate_line(syllable_count=7)
        line3: str = tools.generate_line(syllable_count=5)

        tools.print_with_border([line1, line2, line3])
    except Exception as error:
        print(f"{RED}Error: An unexpected error occurred:{RESET}")
        print(f"{error}")
