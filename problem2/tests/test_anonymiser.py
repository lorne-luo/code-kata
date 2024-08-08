import os
from tempfile import NamedTemporaryFile

from anonymiser import anonymise
from generator import generate_sub_csv


def test_anonymise():
    # generate 1MB source csv
    src_csv_path = generate_sub_csv(1)

    with NamedTemporaryFile(mode="w", newline="", encoding="utf-8") as dst_csv_file:
        anonymise(src_csv_path, dst_csv_file.name)

    os.remove(src_csv_path)
