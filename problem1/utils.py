import logging
import os
from pathlib import Path


def check_file_folder(path: str | Path, delete_old=True):
    if os.path.exists(path):
        if delete_old:
            os.remove(path)
            logging.info(f"Found old fixed width file {path} and removed.")
    else:
        folder = os.path.dirname(path)
        os.makedirs(folder, exist_ok=True)
