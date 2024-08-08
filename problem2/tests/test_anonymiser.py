import os
from tempfile import NamedTemporaryFile

from anonymiser import anonymise, mask_text
from generator import generate_sub_csv


def test_mask_text():
    """test add mask for text"""
    masked_name = mask_text("Firstname")
    assert masked_name == "F********", f"mask text expect F********, got {masked_name}"


def test_anonymise():
    # generate 1MB source csv
    src_csv_path = generate_sub_csv(1)

    with NamedTemporaryFile(mode="w", newline="", encoding="utf-8") as dst_csv_file:
        anonymise(src_csv_path, dst_csv_file.name)

    os.remove(src_csv_path)
