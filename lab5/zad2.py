#Zadanie 2
#Wygeneruj macierz (lista dwupoziomowa) losowych wartości (sprawdź pakiet random) 4x4
# i wykorzystując Python comprehension zdefiniuj listę, która będzie zawierała tylko elementy znajdujące się na głównej przekątnej.
from random import random, randint
macierz = [ [random() for y in range(4)] for x in range(4)]
prz = [ macierz[i][i] for i in range(4)]
print(macierz, prz, sep='\n')