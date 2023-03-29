#Napisz funkcję, która:
#przyjmuje z klawiatury n, będące liczbą całkowitą
#wykonuje n rzutów kostką k6 i zwraca listę krotek wartości postaci ('oczka: 6', 'rzutów: i') itd.,
#  gdzie zmienna i jest ilością rzutów dla tej liczby oczek. Dodaj odpowiedni type hinting.

from random import random, randint
def kostkafu(sc: int) -> list():
    d = dict.fromkeys([a for a in range(1,7)],0)
    for a in range(sc):
        throw = randint(1,6)
        d[throw]+=1
    return [(f'oczka: {a}', f'rzuty: {d[a]}') for a in range(6, 0, -1)]

sc = int(input('Podaj liczbę ile ścianek ma mieć kostka: '))
print(kostkafu(sc))
