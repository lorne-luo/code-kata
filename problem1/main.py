from parser import parse_txt

from generator import generate_txt

if __name__ == '__main__':
    """main entry"""

    # generate fixed width file
    txt_path = generate_txt('data/generated.txt', line_count=10)
    print(f"Print the generated fixed width file {txt_path}:\n")
    with open(txt_path, 'r') as f:
        print(f.read())

    # read the generated fixed width file and dump as csv
    csv_path = parse_txt(txt_path, 'data/parsed.csv')
    print(f"Print the parsed csv file {csv_path}:\n")
    with open(csv_path, 'r') as f:
        print(f.read())
