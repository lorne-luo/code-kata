import os.path
from datetime import datetime

from anonymiser import anonymise
from generator import generate_csv

if __name__ == "__main__":
    src_csv_path = "data/generated.csv"
    dst_csv_path = "data/anonymised.csv"
    csv_size_mb = 20  # 2GB = 2048 MB

    start = datetime.now()
    generate_csv(src_csv_path, csv_size_mb)
    duration = datetime.now() - start
    print(f"CSV generation {src_csv_path} finished in {duration}")

    start = datetime.now()
    anonymise(src_csv_path, dst_csv_path)
    print(f"CSV anonymising {dst_csv_path} finished in {duration}")
