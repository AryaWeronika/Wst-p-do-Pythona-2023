#Zadanie 6
#Napisz skrypt, który z tabeli dostępnej pod adresem http://prawolaffera.pl/uniwersalny-kod-przemowien/ 
# (dane należy zaszyć w skrypcie na stałe) będzie generował n zdań na konsolę. Ilość zdań podawana jest
#  przez użytkownika z klawiatury.
from random import random, randint
zapis = []
zdania = ""
zapis.append(['Koleżanki i koledzy ','Z drugiej strony ','Podobnie ', 'Nie zapominajmy jednak, że ', 'W ten oto sposób ', 'Praktyka dnia codziennego dowodzi, że ', 'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ ', 'Różnorakie i bogate doświadczenia ', 'Troska organizacji, a szczególnie ', 'Wyższe założenia ideowe, a także '])
zapis.append(['realizacja nakreślonych zadań programowych ', 'zakres i miejsce szkolenia kadr ', 'stały wzrost ilości i zakres naszej aktywności ', 'aktualna struktura organizacji ', 'nowy model działalności organizacyjnej ', 'dalszy rozwój różnych form działalności ', 'stałe zabezpieczenie informacyjno programowe naszej działalności ', 'wzmacnianie i rozwijanie struktur ', 'konsultacja z szerokim aktywem ', 'rozpoczęcie powszechnej akcji kształtowania postaw '])
zapis.append(['zmusza nas do przeanalizowania ', 'spełnia istotną rolę w kształtowaniu ', 'wymaga sprecyzowania i określenia ', 'pomaga w przygotowaniu i realizacji ', 'zabezpiecza udział szerokiej grupie w kształtowaniu ', 'spełnia ważne zadania w wypracowaniu ', 'umożliwia w większym stopniu tworzenie ', 'powoduje docenianie wagi ', 'przedstawia intersującą próbę sprawdzenia ', 'pociąga za sobą proces wdrażania i unowocześniania '])
zapis.append(['istniejących warunków administracyjno- finansowych. ', 'dalszych kierunków rozwoju. ', 'systemu powszechnego uczestnictwa. ', 'postaw uczestników wobec zadań stawianych przez organizację. ', 'nowych propozycji. ', 'kierunków postępowego wychowania. ', 'systemu szkolenia kadry odpowiadającego potrzebom. ', 'odpowiednich waruknków aktywizacji. ', 'modelu rozwoju. ', 'form oddziaływania. '])
liczba = int(input('Podaj liczbę zdań: '))

for n in range(liczba):
    for y in range(4):
        random = randint(0, 9)
        zdania += zapis[y][random]
print(zdania)
