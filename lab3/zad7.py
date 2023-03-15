#Wykorzystaj moduł string i następnie:
#wczytaj ze standardowego wejścia dowolny łańcuch znaków,
#używając formatowania znaków wyświetl ile oraz jaki % znaków (zamienionych na małe litery) 
# z wprowadzonego tekstu pokrywa się z: string.ascii_lowercase, string.digits.
import string 


text = input("Wprowadz tekst: \n").lower()
unikalne = list()
for x in text:
    try:
        x = int(x)
    except:
        None
    if x not in unikalne:
        unikalne.append(x)
letters = [x for x in unikalne if type(x) == str if x in [*string.ascii_lowercase]]
digits = [x for x in unikalne if type(x) == int]

print(f'Ten tekst zawiera {len(letters)} unikalnych znaków i stanowi {len(letters)/len(string.ascii_lowercase)*100:.2f}% wszystkich znaków')
print(f'Ten tekst ma {len(digits)} unikalnych cyfr i stanowi {len(digits)/len(string.digits)*100:.2f}% wszystkich liczb')