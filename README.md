# csv-terminal
Terminal reader csv


```java 
usage: main.py [-h] [-f FILE] [-e ENCODING] [-d DELIMITER] [-l] [-n NUMBER_LINES]

Just an example

optional arguments:

  -h, --help  "show this help message and exit"

  -f FILE, --file FILE  "Archivo csv ej: python3 main.py -f 'sample.csv'" (default: "None")

  -e ENCODING, --encoding ENCODING
                        "Tipo de encoding ej: python3 main.py -f 'sample.csv' -e 'utf-8'" (default:
                        "utf8")

  -d DELIMITER, --delimiter DELIMITER
                        "Delimitador dentro del archivo csv ej: python3 main.py -f 'sample.csv' -d ';'"
                        (default: ",")

  -l, --show_lines      "Mostrar lineas separando las filas ej: python3 main.py -f 'sample.csv' -l"
                        (default: "False")

  -n NUMBER_LINES, --number_lines NUMBER_LINES
                        "Numero de lineas del archivo a mostrar ej: python3 main.py -f 'sample.csv' -n 3" (default: "None")

```