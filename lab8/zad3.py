#Zadanie 3
#Napisz kod, który porówna czas wykonania operacji append i append left na obiektu
#typu deque oraz analogicznie append i insert(0) dla obiektu typu list.
from timeit import timeit
from array import array
import random
from datetime import datetime
setup = """
# from collections import deque
# k = deque('Szedl jasiu sciezka'.split())
# """
d1 ="""
# for x in range(100_000):
#     k.append('?')
# """
d2 ="""
# for x in range(100_000):
#     k.append.left('Czy')
# """
print(timeit(d1, setup, number=1))
print(timeit(d2, setup, number=1))

setup = """
# l = 'Szedl jasiu sciezka'.split()
# """
d1="""
# for x in range(100_000):
#     l.append('?')
# """
d2 ="""
# for x in range(100_000):
#     l.insert(0,'Czy')
# """
print(timeit(d1, setup, number=1))
print(timeit(d2, setup, number=1))