import os
from datetime import datetime
from string import ascii_lowercase, ascii_uppercase

from generator import generate_sub_csv
from utils import random_address, random_date, random_name


def test_random_date():
    """test generate a random date"""
    for _ in range(1000):
        # loop to validate correct date generated
        date_str = random_date()
        datetime.strptime(date_str, "%Y-%m-%d")


def test_random_name():
    """test generate a random capital name"""
    for _ in range(1000):
        name = random_name()

        # check length of name
        assert len(name) >= 2
        # check first letter in upper case
        assert name[0] in ascii_uppercase

        # check following letter in lower case
        for ch in name[1:]:
            assert ch in ascii_lowercase


def test_random_address():
    """test random address generation"""
    for _ in range(1000):
        random_address()


def test_generate_sub_csv():
    """generate a temp csv with given size"""
    # generate 1MB temp csv
    size = 1
    tmp_file = generate_sub_csv(size)
    assert os.path.getsize(tmp_file) > 1024 * 1024, f"Generated csv is less than {size}MB specified."
    os.remove(tmp_file)
