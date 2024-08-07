"""
generate a fixed width txt file like below

  f1     f2             f3
 123  ABCDE             11
  12   ABCD          22222
"""

import logging
import os.path
import secrets
from random import randint
from typing import Iterator

from settings import ALIGNMENT, SPECS, AlignmentChoice
from utils import check_file_folder


def get_random_string(max_length: int, nullable=False) -> str:
    """
    Return a securely generated random string which length less than or equal max_length.
    """
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    min_length = 0 if nullable else 1
    length = randint(min_length, max_length)
    return "".join(secrets.choice(allowed_chars) for i in range(length))


def format_to_width(text: str, width: int, alignment=ALIGNMENT) -> str:
    assert width >= 0, f"width {width} should large than 0"
    assert len(text) <= width, f"{text} text length should shorter than width={width}"

    tmpl = f"{{0: <{width}}}" if alignment == AlignmentChoice.Left else f"{{0: >{width}}}"
    return tmpl.format(text)


def generate_cell(width: int) -> str:
    """Generate a random cell content"""
    random_line = get_random_string(width)
    return format_to_width(random_line, width)


def gen_fix_width_line(line_count: int) -> Iterator[str]:
    """generator to create the content of csv file"""

    for i in range(line_count):
        if i == 0 and SPECS["IncludeHeader"] == "True":
            # handle first line
            yield get_header()
        else:
            yield "".join(map(generate_cell, SPECS["Offsets"]))


def get_header() -> str:
    """get the headers line"""
    # create list[(column_name,width)]
    name_and_width = list(zip(SPECS["ColumnNames"], SPECS["Offsets"]))

    # temp lambda to extract positional args from list[(column_name,width)]
    width_format_lambda = lambda name_width_pair: format_to_width(*name_width_pair)

    return "".join(map(width_format_lambda, name_and_width))


def generate_txt(txt_path, line_count: int) -> str:
    """generate fixed width file according to config and return the csv path"""
    check_file_folder(txt_path)

    with open(txt_path, "w", encoding=SPECS["FixedWidthEncoding"]) as file:
        # write row
        for line in gen_fix_width_line(line_count):
            file.write(line + "\n")

    logging.info(f"Fixed width txt file generated at {os.path.abspath(txt_path)}")
    return txt_path
