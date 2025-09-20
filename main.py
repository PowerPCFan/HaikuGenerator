import sys
import modules.tools as tools
from modules.colors.ansi_codes import RED, RESET, YELLOW, BLUE, SUPER_LIGHT_CYAN

if __name__ == "__main__":
    try:
        print(f"{BLUE}Welcome to the Haiku Generator!{RESET}")
        first_run = True
        while True:
            selection = input(
                f"Press {SUPER_LIGHT_CYAN}Enter{RESET} to generate {'a' if first_run else 'another'} haiku, "
                f"or type {SUPER_LIGHT_CYAN}'r'{RESET} to regenerate the Markov model: "
            ).strip().lower()

            if selection == 'r':
                tools.regenerate_markov_model()
            elif selection == '':
                first_run = False
                line1: str = tools.generate_line(syllable_count=5)
                line2: str = tools.generate_line(syllable_count=7)
                line3: str = tools.generate_line(syllable_count=5)

                tools.print_with_border([line1, line2, line3])
            else:
                print(f"{RED}Invalid input. Please try again.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Exiting...{RESET}")
        sys.exit(0)
    except Exception as error:
        print(f"{RED}Error: An unexpected error occurred:{RESET}")
        print(f"{error}")
