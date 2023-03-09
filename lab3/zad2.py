#Zadanie 2
#Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
d=6
lista.pop()
lista.pop()
lista.pop()
lista.pop()
lista.pop()
listaPol = []
for r in range (5):
    lista2.append(d)
    d=d+1
lista2.extend(lista)
print(lista2)
lista2.insert(0,0)
print(lista2)
posortowana = lista2.sort()
print(lista2)
print(posortowana)