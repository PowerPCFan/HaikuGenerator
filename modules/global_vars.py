from modules.config import Config
import sys

try:
    config = Config.load()
except Exception as e:
    print(f"An error occurred when loading configuration: {e}")
    print("Please check your config.json file, or delete it to regenerate defaults.")
    sys.exit(1)
