lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam rutrum in augue ut dapibus. Nulla justo nisl, feugiat non posuere ac, mollis id turpis. Etiam a diam efficitur, rutrum sem vitae, maximus orci. Donec dignissim, dolor non pulvinar maximus, metus turpis fringilla massa, sit amet lobortis augue eros at nisl. Praesent quam dui, varius pellentesque viverra sed, porttitor eu dolor. Phasellus sit amet rutrum nisl. Quisque urna arcu, facilisis in blandit vel, suscipit in nunc. Quisque tellus purus, maximus quis dapibus ac, laoreet non magna. Morbi egestas neque quis purus pulvinar interdum. Sed lacinia a massa ullamcorper interdum. "
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
