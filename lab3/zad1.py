#Zadanie 1Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze
# 5 liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []
d=6
lista.pop()
lista.pop()
lista.pop()
lista.pop()
lista.pop()
for r in range (5):
    lista2.append(d)
    d=d+1
print("Druga lista ", lista2)
print("Pierwsza lista ", lista)