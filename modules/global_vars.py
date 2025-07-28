from modules.config import Config

config = Config.load()

ANSI: str = "\033["
GREEN: str = ANSI + "32m"
RED: str = ANSI + "31m"
GREY: str = ANSI + "38;5;245m"
RESET: str = ANSI + "0m"
