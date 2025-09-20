import json
import os
from dataclasses import dataclass

CONFIG_JSON = "config.json"


@dataclass
class Config:
    spell_check: bool

    @staticmethod
    def load(json_path="config.json") -> "Config":
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Error: {json_path} not found.")
        with open(json_path) as f:
            data = json.load(f)
        return Config(**data)
