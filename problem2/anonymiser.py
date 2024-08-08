import csv
import logging
import os

from settings import DELIMITER
from utils import check_file_folder, timing


def mask_text(txt: str) -> str:
    """use * replace sensitive text"""
    words = txt.split(' ')
    length = len(txt)
    return txt[0] + '*' * (length - 1)


@timing
def anonymise(src_csv_path: str, dst_csv_path: str) -> str:
    if not os.path.isfile(src_csv_path):
        msg = f"src_csv_path {src_csv_path} is not exist"
        logging.exception(msg)
        raise FileNotFoundError(msg)

    check_file_folder(dst_csv_path)

    with open(src_csv_path, "r", encoding="utf-8") as src_csv_file, open(
            dst_csv_path, "w", encoding="utf-8"
    ) as dst_csv_file:
        src_reader = csv.reader(src_csv_file, delimiter=DELIMITER)
        dst_csv_writer = csv.writer(dst_csv_file, delimiter=DELIMITER, quoting=csv.QUOTE_MINIMAL)

        line_count = 0
        for row in src_reader:
            line_count += 1
            # first line for header
            if line_count == 1:
                dst_csv_writer.writerow(row)
                continue

            # anonymise a row and dump
            anonymised_row = [mask_text(row[0]), mask_text(row[1]), mask_text(row[2]), row[3]]
            dst_csv_writer.writerow(anonymised_row)

    return dst_csv_path
