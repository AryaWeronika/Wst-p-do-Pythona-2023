#Napisz kod, w którym wykorzystasz poniższe metody dla typów:
#int.bit_count()
#float.is_integer()

bits = [1, 5]
fis = [5.6, 8.4]

for x in bits:

    if (n := bin(x).count("1")) > 1:  
        print("Zmienna \"" + str(x) + "\" ma wiecej niz jeden bit. Zmienna ma " + str(n) + " bitow.")
for x in fis:
    if x.is_integer():
        print("Zmienna \"" + str(x) + "\" moze byc int.")