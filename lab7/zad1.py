#Zadanie 1
#Wykorzystując wbudowaną funkcję isinstance oraz filter napisz funkcję extract_numbers(vals: list[Any]) -> list[int | float],
# która z podanej listy dowolnych obiektów odfiltruje tylko obiekty typu int oraz float i zwróci listę je zawierającą.
def extract_numbers():
    lista = [1, 2, 3, 4, 3.2, "sad", "asda", 3.8]
    for x in range(0, 7):
        if isinstance(lista[x], int) is True:
            print(lista[x])
        if isinstance(lista[x], float) is True:
            print(lista[x])

extract_numbers()
