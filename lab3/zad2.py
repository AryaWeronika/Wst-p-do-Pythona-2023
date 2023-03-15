#Zadanie 3
#Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funckję input(). 
# Następnie wyświetl ciąg unikalnych znaków z wczytanego zdania,
#  zapisanych alfabetycznie małymi literami.
import numpy as np
zdanie = input('Wpisz jakiś tekst: \n')
#words = zdanie.split(' ')
words = np.array([*zdanie])
unikalne = list()
print(words)
for x in words:
    if x not in unikalne:
        unikalne.append(x)
#unikalne.lower()
print(unikalne)