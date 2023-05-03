#Zadanie 1
#Wykorzystując przykład z listingu 2 napisz kod, który przetestuje czas inicjowania
# tablicy znaków oraz wartości całkowitych (typ int i long) i porówna z czasem zainicjowania listy z takimi samymi wartościami.
# test czasu wykonania
# test czasu wykonania
from timeit import timeit
import random

setup = """
# from array import array
# import random
# """
d1 = """
# tab_of_ints = array('I', [random.randint(0,255) for _ in range(1_000_000)])
# """
d2 = """
# list_of_ints = [random.randint(0,255) for _ in range(1_000_000)]
# """



d3 = """
# tab_of_ints = array('B', [random.randint(0,255) for _ in range(1_000_000)])
# """
d4 = """
# list_of_ints = [random.randint(0,255) for _ in range(1_000_000)]
# """
print(timeit(d2, setup, number=100))
print(timeit(d1, setup, number=100))
print(timeit(d3, setup, number=100))
print(timeit(d4, setup, number=100))