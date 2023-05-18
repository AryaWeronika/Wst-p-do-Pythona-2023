#Zadanie 2
#Napisz funkcję, która odczyta wszystkie pliki .txt z podanego folderu i podfolderów
# (testuj na zasobie dane_do_lab_10.zip) i scali ich zawartość do jednego pliku .csv,
# pomijając duplikujące się nagłówki występujące w plikach.
# odczytanie listy zasobów w bieżącym folderze (domyślna ścieżka)
import os
import csv
import glob

def merge_txt_files_to_csv(folder_path, output_file):
    # Tworzenie nowego pliku CSV
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Znajdowanie plików .txt w podfolderach
        txt_files = glob.glob(os.path.join(folder_path, '**/*.txt'), recursive=True)

        # Iterowanie przez znalezione pliki
        for file_path in txt_files:
            with open(file_path, 'r') as txt_file:
                lines = txt_file.readlines()

                # Pomijanie nagłówka, jeśli jest już obecny w pliku CSV
                if lines[0] == 'header\n':
                    lines = lines[1:]

                # Zapisywanie zawartości pliku do pliku CSV
                writer.writerows(csv.reader(lines))

    print(f"Scalono pliki .txt do pliku {output_file}")

    merge_txt_files_to_csv('data_for_lab_10', 'output.csv')