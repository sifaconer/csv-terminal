import csv
import random
import sys
import argparse


class Colors:
    BLACK = '\033[30m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    BG_LIGHTGREY = '\033[48;5;239m'

    @staticmethod
    def font_black(msg=""):
        return f'{Colors.BLACK}{msg}'

    @staticmethod
    def font_bold(msg=""):
        return f'{Colors.BOLD}{msg}'

    @staticmethod
    def font_fail(msg=""):
        return f'{Colors.FAIL}{msg}'

    @staticmethod
    def font_reset():
        return f'{Colors.ENDC}'

    @staticmethod   
    def bg_font_color(msg):
        return f'{Colors.BG_LIGHTGREY}{msg}'


def read_csv(filename, encoding='utf-8', delimiter=',', nro_lines=None, decore=False):
    """
    Reads a CSV file
    """
    try:
        has_header = False
        with open(filename, 'r', encoding=encoding, newline='', errors='ignore') as f:
            reader = csv.reader(f, delimiter=delimiter, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            sample = f.read(4064)
            has_header = csv.Sniffer().has_header(sample)

        with open(filename, 'r', encoding=encoding, newline='', errors='ignore') as f:
            reader = csv.reader(f, delimiter=delimiter, quoting=csv.QUOTE_ALL, skipinitialspace=True)
            print_csv(filename, reader, nro_lines, decore=decore, has_header=has_header)

    except Exception as e:
        raise SystemExit(f"{Colors.font_fail(Colors.font_bold('[ERROR]:'))} {Colors.font_reset()} {e}")


def print_header(header=[], format_row=""):
    """
    Print header of the table
    """
    header_format = "-" * (len(format_row.format("", *header))+1)
    print("┌"+header_format+"┐")
    print(" "+Colors.bg_font_color(format_row.format(*header)), Colors.font_reset())
    print("└"+header_format+"┘")


def print_row(format_row="", row=[], decore=False, color=False):
    """
    Print a row of the table
    """
    sub_line=""
    if decore:
        sub_line = "-" * (len(format_row.format("", *row))+1)
        sub_line = "├"+sub_line+"┤"

    if decore is False and color:   
        print(" "+Colors.bg_font_color(format_row.format(*row)), Colors.font_reset(), end="")
    else:
        print(" "+format_row.format(*row), end="")
    print("\n"+sub_line)


def get_header(reader, has_header=False):
    """
    Load the header file if not exist return array with lines 
    """
    header = []
    # Get first row with header
    for row in reader:
        if has_header:
            header = row
            break
        else:
            for _ in row:
                header.append("---")
            break

    return header


def calc_format(reader, len_header):
    """
    Calculate the format of the header table
    """
    string_format = "{:^14} " * len_header
    array_format = string_format.split(" ")[:-1]
    list_from_csv = list(reader)
    list_sectors = [
        list_from_csv[0], 
        list_from_csv[random.randint(0, len(list_from_csv)-1)],
        list_from_csv[random.randint(0, len(list_from_csv)-1)], 
        list_from_csv[random.randint(0, len(list_from_csv)-1)], 
        list_from_csv[-1]
        ]

    last_value = 14
    for row in list_sectors:
        for i in range(len(row)):
            if len(str(row[i])) >= 50:
                continue
            if last_value < len(str(row[i])):
                array_format[i] = '{:^'+str(len(str(row[i])))+'}'
                last_value = len(str(row[i]))

    return "".join(array_format), list_from_csv
        

def print_resume(list_element, header, filename):
    """
    Print the resume information for CSV file contents
    """
    archivo = "Archivo: " + filename
    total_rows = "Total filas: " + str(len(list_element)+1)
    total_columns = "Total columnas: " + str(len(list_element[0]))
    list_header = "Cabeceras: "+" ".join(header)

    format_row = ""
    if len(list_header) >= len(archivo):
        format_row = "{:^"+str(len(list_header)+1)+"}"
    else:
        format_row = "{:^"+str(len(archivo)+1)+"}"

    header_format = "-" * (len(format_row.format("", total_rows))+1)
    print("┌"+header_format+"┐")
    print("| " + str(archivo) + str(" " * ((len(header_format)-len(archivo)) - 1)) + "|")
    print("| " + str(total_columns) + str(" " * ((len(header_format)-len(total_columns)) - 1)) + "|")
    print("| " + str(total_rows) + str(" " * ((len(header_format)-len(total_rows)) - 1)) + "|")
    print("| " + str(list_header) + str(" " * ((len(header_format)-len(list_header)) - 1)) + "|")
    print("└"+header_format+"┘")


def print_csv(filename, reader, limit, has_header=True, decore=False):
    """
    Organizes a CSV file information
    """
    header = get_header(reader, has_header)
    format_row, list_element = calc_format(reader, len(header))
    
    print_resume(list_element, header, filename)

    print_header(header, format_row) # Print header

    row_count = 1
    for row in list_element[:limit]:
        if row_count % 2 == 0:
            print_row(format_row,row, decore,  True)
        else:
            print_row(format_row, row, decore, False)
        row_count += 1


def main():
    text_descriptions = {
        'file': 'Archivo csv ej: python3 main.py -f "sample.csv"',
        'encoding': 'Tipo de encoding ej: python3 main.py  -f "sample.csv" -e "utf-8"',
        'delimiter': 'Delimitador dentro del archivo csv ej: python3 main.py  -f "sample.csv" -d ";"',
        'show_lines': 'Mostrar lineas separando las filas ej: python3 main.py  -f "sample.csv" -l',
        'number_lines': 'Numero de lineas del archivo a mostrar ej: python3 main.py  -f "sample.csv" -n 3'
    }

    parser = argparse.ArgumentParser(
        description="Just an example",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-f", "--file", default=None, type=str, help=text_descriptions['file'])
    parser.add_argument("-e", "--encoding", default="utf8", type=str, help=text_descriptions['encoding'])
    parser.add_argument("-d", "--delimiter", default=",", type=str, help=text_descriptions['delimiter'])
    parser.add_argument("-l", "--show_lines", action='store_true', help=text_descriptions['show_lines'])
    parser.add_argument("-n", "--number_lines", default=None, type=int, help=text_descriptions['number_lines'])
    args = parser.parse_args()
    config = vars(args)

    if config["file"] is not None:
        read_csv(
            filename=config["file"], 
            encoding=config["encoding"], 
            delimiter=config["delimiter"], 
            nro_lines=config["number_lines"], 
            decore=config["show_lines"]
        )
    else:
        raise SystemExit(f"No existe archivo, Ej: {sys.argv[0]} -f \"sample.csv\"")


if __name__ == '__main__':
    main()
