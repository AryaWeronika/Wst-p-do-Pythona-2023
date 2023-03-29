#Napisz funkcję, która przyjmuje nieokreśloną liczbę wartości z kluczem. Funkcja przyjmuje argumenty w postaci: 
# klucz to nazwa drużyny a wartość to ilość punktów, które drużyna zdobyła. Funkcja zlicza, ile jest wszystkich punktów razem
# i zwraca tę wartość.
def liczba(** teams: dict()) -> int:
    return sum([teams[x] for x in teams])

print(liczba(red = 4, blue = 2, yellow = 7, black = 1))     