#Zadanie 5
#Napisz funkcję, która:
#przyjmuje następujące argumenty: nazwa pliku, indeks kolumny z datą, format źródłowy i docelowy. Odczytaj plik z zadania
# 2 i skonwertuj datę na format 'RRRR-MM-DD'. Zapisz plik pod inną nazwą.
import csv
from datetime import datetime

def convert_date_format(file_name, date_column_index, source_format, target_format):
    # Wczytanie danych z pliku źródłowego
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Konwersja daty w każdym wierszu
    for row in rows:
        if len(row) > date_column_index:
            source_date_str = row[date_column_index]

            # Parsowanie daty z formatu źródłowego
            source_date = datetime.strptime(source_date_str, source_format)

            # Konwersja daty na format docelowy
            target_date_str = source_date.strftime(target_format)

            # Aktualizacja wartości wiersza
            row[date_column_index] = target_date_str

    # Tworzenie nowej nazwy pliku
    file_name_parts = file_name.split('.')
    new_file_name = f"{file_name_parts[0]}_converted.{file_name_parts[1]}"

    # Zapisywanie danych do nowego pliku
    with open(new_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Konwersja zakończona. Plik zapisany jako: {new_file_name}")

file_name = 'pliczek.csv'
date_column_index = 2
source_format = '%d/%m/%Y'  # Format źródłowy, np. 'dd/mm/yyyy'
target_format = '%Y-%m-%d'  # Format docelowy, np. 'yyyy-mm-dd'

convert_date_format(file_name, date_column_index, source_format, target_format)