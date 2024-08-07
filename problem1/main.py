from generator import generate_txt
from parser import parse_txt

if __name__ == '__main__':
    txt_path = generate_txt('data/generated.txt', line_count=10)

    parse_txt(txt_path, 'data/parsed.csv')
