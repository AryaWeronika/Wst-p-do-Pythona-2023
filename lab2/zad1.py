# Napisz fragment kodu, który wczyta trzy zmienne z klawiatury:
# linię danych rozdzielonych jakimś separatorem (spacja, średnik, itd.)
# separator źródłowy
# separator docelowy
sentence = input('Wpisz dowolne zdanie:\n')
words = sentence.split(' ')
sep = input('Podaj separator: \n')
x = sep.join(sentence)
print(x)