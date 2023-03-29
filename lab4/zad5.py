#Zadanie 5
#Napisz skrypt, który pobiera z klawiatury zdanie, a na konsoli wyświetla wyrazy z tego zdania
#  posortowane według ich długości rosnąco.

tekst = input('Wpisz dowolne zdanie: ')
tekst.split(" ")
#dlugosc = len(split_text)
sorted(tekst, key=len)
print(sorted(tekst, key=len))