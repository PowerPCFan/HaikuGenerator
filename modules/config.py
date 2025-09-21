import json
import os
from dataclasses import dataclass

CONFIG_JSON = "config.json"

DEFAULT_CONFIG = {
    "max_generation_attempts": 100,
    "advanced_spell_check": False,
    "syllables": [5, 7, 5],
    "state_size": 2
}


@dataclass
class Config:
    max_generation_attempts: int
    advanced_spell_check: bool
    syllables: list[int]
    state_size: int

    @staticmethod
    def load(json_path="config.json") -> "Config":
        if not os.path.exists(json_path):
            Config._create_default_config(json_path)
            return Config(**DEFAULT_CONFIG)

        try:
            with open(json_path) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading {json_path}: {e}. Creating new config file.")
            Config._create_default_config(json_path)
            return Config(**DEFAULT_CONFIG)

        for key, default_value in DEFAULT_CONFIG.items():
            if key not in data:
                print(f"Key '{key}' was not found in your config file, adding default value.")
                data[key] = default_value

                try:
                    with open(json_path, "w") as f:
                        json.dump(data, f, indent=4)
                except IOError as e:
                    print(f"Error saving updated config: {e}")

        return Config(**data)

    @staticmethod
    def _create_default_config(json_path="config.json") -> None:
        try:
            with open(json_path, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            print(f"Created new config file: {json_path}")
        except IOError as e:
            print(f"Error creating config file: {e}")

    @staticmethod
    def _remove_config_file(json_path="config.json") -> None:
        try:
            if os.path.exists(json_path):
                os.remove(json_path)
        except IOError as e:
            print(f"Error removing config file: {e}")

    def save(self, json_path="config.json") -> None:
        try:
            with open(json_path, "w") as f:
                json.dump(self.__dict__, f, indent=4)
        except IOError as e:
            raise IOError(f"Error saving config file: {e}")
