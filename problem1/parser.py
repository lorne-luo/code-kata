"""
parse below generated fixed width txt file:
  f1     f2             f3
 123  ABCDE             11
  12   ABCD          22222

then dump as csv:

f1,f2,f3
123,ABCDE,11
12,ABCD,22222
"""

import csv
import logging

from settings import SPECS, DELIMITER
from utils import check_file_folder


def parse_line(line: str) -> list[str]:
    """parse str line into a list of cell"""
    cells = []
    start = 0
    for width in SPECS["Offsets"]:
        content = line[start: start + width]
        cells.append(content.strip())
        start += width

    return cells


def parse_txt(txt_path: str, csv_path: str) -> str:
    """parse the fixed width file line by line and save into csv"""
    # open both fixed width txt file and the target csv
    check_file_folder(csv_path)

    try:
        with open(txt_path, "r", encoding=SPECS["FixedWidthEncoding"]) as txt_file, \
                open(csv_path, "w", encoding="utf8") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=DELIMITER, quoting=csv.QUOTE_MINIMAL)

            while True:
                line = txt_file.readline()
                if not line:
                    # reach the end, jump out
                    break

                row = parse_line(line)
                csv_writer.writerow(row)
    except FileNotFoundError:
        logging.exception(f"txt file {txt_path} not exist")
    return csv_path
