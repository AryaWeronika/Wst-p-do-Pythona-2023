#Zadanie 3
#Napisz skrypt, który pobiera od użytkownika wartość liczbową,
#  a następnie wyświetla na konsoli zdanie w postaci: "Podaną liczbę można zapisać jako: ...", 
# gdzie zapis będzie w postaci sumy iloczynów liczb dla każdego rzędu. Np. liczba 123: "Podaną liczbę można zapisać jako:
#  100 * 1 + 10 * 2 + 1 * 3". Do pobrania i wypisania wartości użyj odpowiednio instrukcji readline() i write() z modułu sys).
#print('Podaj liczbę: \n')
#s = sys.stdin.readline()
import sys

print('Podaj liczbę: \n')
try:
    liczba = int(sys.stdin.readline())
    mt = pow(10,(len(str(liczba))-1))
    zapis = f"Podaną liczbę można zapisać jako: "
    while liczba > 0:
        temp = int(liczba//mt)
        zapis+=f'{mt} * {temp}'
        if(mt > 1):
            zapis+=f' + '
        liczba = liczba - (temp*mt)
        mt= int(mt/10)
    sys.stdout.write(zapis)
except:
    print('To nie jest liczba \n')