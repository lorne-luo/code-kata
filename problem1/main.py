from generator import generate_txt
from parser import parse_txt

if __name__ == '__main__':
    txt_path = generate_txt('generated.txt', line_count=50)

    parse_txt(txt_path,'parsed.csv')
