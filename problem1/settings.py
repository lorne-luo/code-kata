import logging
# orjson is a C implemented json parser, much faster than built-in json module
import os.path
from enum import Enum

import orjson as json


def get_config(config_path: str) -> dict:
    try:
        with open(config_path) as f:
            config = json.loads(f.read())

            try:
                # convert offset to int
                config["Offsets"] = list(map(int, config["Offsets"]))
            except ValueError:
                logging.exception("Offsets should all in integer.")

            return config
    except FileNotFoundError:
        abspath = os.path.abspath(config_path)
        logging.exception(f"Config file {abspath} not found.")


class AlignmentChoice(Enum):
    Left = 1
    Right = 2


CONFIG_PATH = "../spec.json"

SPECS = get_config(CONFIG_PATH)

ALIGNMENT = AlignmentChoice.Right

DELIMITER = ","
