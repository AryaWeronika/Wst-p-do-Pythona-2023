#Zadanie 4
#Wykorzystaj moduł this i korzystając z umieszczonego tam słownika kodującego
# (sprawdź dostępne zmienne modułu this) napisz skrypt, który będzie kodował tym słownikiem wpisywane zdanie 
# (przechwytuj z klawiatury). Wypisuj na konsoli zakodowane zdanie.
import this
tekst = input('Wpisz tekst: ')
kodtekst = ""
for n in tekst:
    kodtekst += this.d[n]

print('zakodowany kod to: ',kodtekst)