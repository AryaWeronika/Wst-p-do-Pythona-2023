#Zadanie 2
#Wykorzystując funkcję sorted i funkcję anonimową (lambda) posortuj listę wyrazów (wprowadzaną przez input) według ilości znaków w wyrazie malejąco.

tekst = input('wprowadz tekst')
slowa = tekst.split(' ')
print(slowa)
#print(sorted(slowa))
print(sorted(slowa, key=lambda x: x.lower(), reverse = True))