#Zadanie 1
#Pobieraj z klawiatury wartość w postaci liczby całkowitej, a następnie wyświetl ją w postaci liczby binarnej, ósemkowej i szesnastkowej.
liczba = input('Podaj liczbę całkowitą: \n')
def DecimalToBinary(liczba):
    in2 = int(liczba)
    if in2 >= 1:
        DecimalToBinary(in2 // 2)
    print(in2 % 2, end = '')
#DecimalToBinary(liczba)
dec = int(liczba)

print("Liczba całkowita", dec, "to:")
print(bin(dec), "in binarna.")
print(oct(dec), "to ósemkowa.")
print(hex(dec), "to szestnastkowa.")