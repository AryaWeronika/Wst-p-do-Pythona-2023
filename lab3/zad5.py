#Zadanie 5
#Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy. Połącz teraz słowniki tak, żeby 
# przykładowo dla kwietnia, dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

slownik = {}
slownik2 ={}
slownik = dict([('styczen', 1), ('luty', 2), ('marzec', 3), ('kwiecien', 4), ('maj', 5), ('czerwiec', 6), ('lipiec', 7), ('sierpien', 8), ('wrzesien', 9), ('pazdziernik', 10), ('listopad', 11), ('grudzien', 12)])
slownik2 = dict([('january', 1), ('february', 2), ('march', 3), ('april', 4), ('may', 5), ('june', 6), ('july', 7), ('august', 8), ('september', 9), ('october', 10), ('november', 11), ('december', 12)])
print(slownik)


print(slownik2)

razem = dict()
razem['pl'] = slownik
razem['en'] = slownik2

print(razem['pl'][4], razem['en'][4])