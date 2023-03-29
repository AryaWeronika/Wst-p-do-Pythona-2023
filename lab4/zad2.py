#Napisz skrypt, który pobiera od użytkownika wartość i:
#sprawdzaj czy podana wartość jest rzutowalna na typ int i float i wyświetl stosowne komunikaty.
i = input('Podaj wartość i: \n')
try:
    liczba = float(i)
    print(liczba)
except ValueError:
    print ("To nie może być float")
try:
    liczba2 = int(i)
    print(liczba2)
except ValueError:
    print ("To nie może być int")
