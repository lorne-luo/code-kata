from parser import parse_line

import pytest

from generator import (format_to_width, gen_fix_width_line, get_header,
                       get_random_string)
from settings import CONFIG_PATH, AlignmentChoice, get_config


def test_parse_line() -> None:
    """get config as dict"""
    line = "    a          kd Q5 s       2W3DI8 FGO6W0 LEDrHYk5u   ChWjwlwtn9            dLgRLqof cwksk2zhDAMC"
    cells = parse_line(line)
    expect_cells = ["a", "kd", "Q5", "s", "2W3DI8", "FGO6W0", "LEDrHYk5u", "ChWjwlwtn9", "dLgRLqof", "cwksk2zhDAMC"]
    for i, v in enumerate(cells):
        assert cells[i] == expect_cells[i], f"Line parse error, expect {expect_cells}, got {cells}"
