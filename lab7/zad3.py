#Zadanie 3
# funkcję sorted napisz funkcję, która będzie sortowała listę zawierająca wartości typu int oraz str (może wystąpić tylko jeden lub oba typy danych).
# Funkcja posiada atrybut domyślny reversed=False, który oznacza, że zwrócona lista będzie najpierw zawierała liczby posortowane rosnąco, a następnie
# łańcuchy znaków. Wartość True tego atrybutu oznaczać będzie w liście wyjściowej najpierw łańcuchy znaków, a później liczby.
lista = [1, 2, 3, 4, 3.2, "sad", "asda", 3.8]
listaint = []
listastr = []

for x in range(0, 7):
        if isinstance(lista[x], int) is True:
            listaint.append(lista[x])
        if isinstance(lista[x], str) is True:
            listastr.append(lista[x])

sorted(listaint)
print(listaint)
sorted(listastr)
print(listastr)
joined = []
joined.extend(listaint)
joined.extend(listastr)
print(joined)