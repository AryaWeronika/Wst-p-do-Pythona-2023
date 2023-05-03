
from collections import deque, namedtuple, Counter
# #Zad 6
def tab(*args):
    return deque(Counter(args).elements())


print(tab(4,5,6,7,4,6,2,7,4,5,6,6,5,3,5,5,3,4,5,1))