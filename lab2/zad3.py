
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
#Korzystając ze zmiennej z zadania 2 wyświetl na konsoli tekst postaci:
# „W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}” .
# W miejsca {liczba_liter1} oraz {liczba_liter2} podstaw zmienne, które będą przechowywały
# liczbę wystąpień danych liter (poszukaj odpowiedniej metody dla typu str). Litery, które
# należy wyszukać to 4-ta litera nazwiska oraz 3-cia litera imienia osoby wykonującej ćwiczenie,
# np. imie = „Jan”, nazwisko = „Kowalski”, litera_1 = imie[2], litera_2 = nazwisko[3].
imie = "Weronika"
nazwisko = "Kowacka"
litera_1 = imie[2]
litera_2 = nazwisko[3]
print(litera_1,litera_2)
words = lorem.split(litera_1)
ileR= len(words)-1
print(ileR)
words = lorem.split(litera_2)
ileA= len(words)-1
print(ileA)
print("W tekście jest ",ileR, "liter ",litera_1," oraz ",ileA," liter ",litera_2)