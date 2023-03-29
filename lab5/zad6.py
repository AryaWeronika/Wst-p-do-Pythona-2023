#Zadanie 6
#Wykorzystując poprzedni przykład z listingu 11 zdefiniuj funkcję, która będzie przyjmowała
#  obiekty typu str jako wejście (dowolną liczbę), a będzie zwracała listę tych łańcuchów posortowaną alfabetycznie.
def alphabetic(* tekst: str) -> list():
    if len(tekst) == 0:
        return list()
    else:
        return sorted([ n for n in tekst ])
    
print(alphabetic('alfa', 'beta', 'a', 'ba', 'bz'))