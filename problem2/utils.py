import logging
import os
from functools import wraps
from pathlib import Path
from random import choice, randint
from string import ascii_lowercase, ascii_uppercase
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print("func:%r args:[%r, %r] took: %2.4f sec" % (f.__name__, args, kw, te - ts))
        return result

    return wrap


def check_file_folder(file_path: str | Path, delete_old=True):
    if os.path.isdir(file_path):
        raise FileExistsError(f"A directory with given file path {file_path} already existed.")
    if os.path.exists(file_path):
        if delete_old:
            os.remove(file_path)
            logging.info(f"Found old fixed width file {file_path} and removed.")
    else:
        folder = os.path.dirname(os.path.abspath(file_path))
        os.makedirs(folder, exist_ok=True)


def random_date() -> str:
    """fast generate a datetime str like 2024-11-03"""
    year = randint(1970, 2024)
    month = randint(1, 12)
    day = randint(1, 28)
    return f"{year}-{month:0>2}-{day:0>2}"


def random_name(max_length: int = 10) -> str:
    """random generate a name"""
    length = randint(2, max_length)
    first_letter = choice(ascii_uppercase)
    following_letters = "".join([choice(ascii_lowercase) for _ in range(length - 1)])
    return first_letter + following_letters


def random_address():
    """
    generate a fake Aus address, format like:

    99 Name Rd Suburb, STATE 9999
    """
    numbers = randint(1, 999)
    rode_types = ("St", "Rd", "Ct")  # todo add more
    states = ("ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA")
    postcodes = randint(200, 9999)

    return f"{numbers} {random_name()} {choice(rode_types)} {random_name()}, {choice(states)} {postcodes:0>4}"
