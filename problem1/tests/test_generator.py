import pytest

from generator import format_to_width, get_header, gen_fix_width_line, get_random_string
from settings import CONFIG_PATH, get_config, AlignmentChoice


def test_config() -> None:
    """get config as dict"""
    config = get_config(CONFIG_PATH)
    assert type(config) is dict


def test_generate_random_string() -> None:
    """test random string generation"""
    config = get_config(CONFIG_PATH)
    for length in config["Offsets"]:
        length = int(length)
        random_string = get_random_string(max_length=length)
        assert len(random_string) <= length


def test_width_format() -> None:
    """test content be formatted into expected width and alignment"""
    assert " xxx" == format_to_width("xxx", 4, AlignmentChoice.Right), "right alignment format not as expected"
    assert "xxx  " == format_to_width("xxx", 5, AlignmentChoice.Left), "left alignment format not as expected"

    with pytest.raises(Exception):
        format_to_width("xxx", 2, AlignmentChoice.Right)


def test_get_header():
    """make sure generate correct column header"""
    header = get_header()
    expect_harders = [
        "   f1",
        "          f2",
        " f3",
        "f4",
        "           f5",
        "     f6",
        "        f7",
        "           f8",
        "                  f9",
        "          f10",
    ]
    expect_harder_line = "".join(expect_harders)
    assert header == expect_harder_line, f"Header is wrong, got {header}, expect {expect_harder_line}"


def test_content_generator():
    """generate fixed width file with given line count"""
    csv_lines = list(gen_fix_width_line(2))
    assert len(csv_lines) == 2
