#Zadanie 5
#Napisz funkcję, która z tablicy wartości liczbowych będzie zwracała 10% najwyższych wartości.
from array import array
import random
tab = sorted(array('I', [random.randint(0,1000000) for _ in range(1000)]))
print(tab[len(tab):len(tab)-int(len(tab)/10)-1:-1])