import logging

# orjson is a C implemented json parser, much faster than built-in json module
import orjson as json
from enum import Enum


def get_config(config_path: str) -> dict:
    with open(config_path) as f:
        config = json.loads(f.read())

        try:
            # convert offset to int
            config["Offsets"] = list(map(int, config["Offsets"]))
        except ValueError:
            logging.exception("Offsets should all in integer.")

        return config


class AlignmentChoice(Enum):
    Left = 1
    Right = 2


CONFIG_PATH = "../spec.json"

SPECS = get_config(CONFIG_PATH)

ALIGNMENT = AlignmentChoice.Right

DELIMITER = ","
