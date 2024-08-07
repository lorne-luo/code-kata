import pytest

from generator import format_to_width, get_header, gen_fix_width_line, get_random_string
from parser import parse_line
from settings import CONFIG_PATH, get_config, AlignmentChoice


def test_parse_line() -> None:
    """get config as dict"""
    line = "    a          kd Q5 s       2W3DI8 FGO6W0 LEDrHYk5u   ChWjwlwtn9            dLgRLqof cwksk2zhDAMC"
    cells = parse_line(line)
    expect_cells = ["a", "kd", "Q5", "s", "2W3DI8", "FGO6W0", "LEDrHYk5u", "ChWjwlwtn9", "dLgRLqof", "cwksk2zhDAMC"]
    for i, v in enumerate(cells):
        assert cells[i] == expect_cells[i], f"Line parse error, expect {expect_cells}, got {cells}"
