#Zadanie 1
#Napisz funkcję, która będzie przyjmowała listę ścieżek do folderów. Następnie iterując przez listę
# sprawdzaj, czy dana ścieżka istnieje i jeżeli nie to twórz wszystkie niezbędne foldery (i podfoldery).
# Sprawdź możliwość metody makedirs z modułu os.
import os

def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Utworzono folder: {path}")
        else:
            print(f"Folder już istnieje: {path}")
folders = ["folder1", "folder2/subfolder1", "folder3/subfolder2"]
create_folders(folders)