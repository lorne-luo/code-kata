"""
generate a CSV with four columns ["first_name", "last_name", "address", "dob"]

fill cell with random text

"""

import csv
import logging
import os
import sys
from tempfile import NamedTemporaryFile
from typing import Sequence

from ray.util.multiprocessing import Pool

from settings import DELIMITER, HEADERS
from utils import random_address, random_date, random_name, timing


def generate_line() -> Sequence[str]:
    first_name = random_name()
    last_name = random_name()
    address = random_address()
    dob = random_date()
    return first_name, last_name, address, dob


def calc_file_size(line_items):
    """calculate how many file size added in bytes for a csv row"""
    line_text = DELIMITER.join(line_items)
    utf8_header_size = sys.getsizeof("".encode("utf-8"))
    line_size = sys.getsizeof(line_text.encode("utf-8"))
    return line_size - utf8_header_size


@timing
def generate_sub_csv(size_mb: int) -> str:
    """
    generate csv file with given size

    size_mb: MB to generate
    """

    total_bytes = 0
    with NamedTemporaryFile(delete=False, mode="w", newline="", encoding="utf-8") as csv_file:
        print(csv_file.name)
        csv_writer = csv.writer(csv_file, delimiter=DELIMITER, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(HEADERS)
        line_count = 1

        while total_bytes < size_mb * 1024 * 1024:
            # generate a line
            line_items = generate_line()

            line_bytes = calc_file_size(line_items)
            total_bytes += line_bytes
            line_count += 1

            csv_writer.writerow(line_items)
    print(csv_file.name, f"size={total_bytes / 1024}, line={line_count}")
    return csv_file.name


def merge_csv(merged_csv_path: str, sub_csv_paths: list[str]) -> str:
    logging.info(f"Mergeing into {merged_csv_path}")

    line_count = 0
    with open(merged_csv_path, "w", newline="", encoding="utf-8") as dest_file:
        csv_writer = csv.writer(dest_file, delimiter=DELIMITER, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(HEADERS)

        for sub_csv_path in sub_csv_paths:
            try:
                with open(sub_csv_path, "r", newline="", encoding="utf-8") as sub_csv_file:
                    reader = csv.reader(sub_csv_file)
                    # skip header
                    next(reader)
                    for row in reader:
                        csv_writer.writerow(row)
                        line_count += 1
                file_size = os.path.getsize(sub_csv_path)
                logging.info(f"Delete merged csv {sub_csv_path}, size={file_size / 1024}")
                print(f"Delete merged csv {sub_csv_path}, size={file_size / 1024}")
                os.remove(sub_csv_path)
            except Exception as ex:
                # log error and continue
                logging.exception(ex)
        print(f"total line is {line_count}")
    return merged_csv_path


@timing
def generate_csv(csv_path: str, size_mb: int) -> str:
    core_count = os.cpu_count()
    if not core_count:
        core_count = 1
    mb_per_core = size_mb / core_count

    print(f"core_count={core_count}, mb_per_core={mb_per_core}")
    pool = Pool(core_count)
    sub_csv_paths = pool.map(generate_sub_csv, [mb_per_core] * core_count)
    merged_csv_path = merge_csv(csv_path, sub_csv_paths)

    abs_path = os.path.abspath(merged_csv_path)
    print(abs_path)
    return abs_path


if __name__ == "__main__":
    csv_size_mb = 256  # 2GB = 2048 MB
    generate_csv("generated.csv", csv_size_mb)
    # generate_sub_csv(256)
