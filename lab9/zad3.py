class Point:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point({self.x},{self.y}) '
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

#Zadanie 3
#Sprawdź, czy możliwe jest pomnożenie obiektu typu Point przez wartość
# całkowitoliczbową. Zaimplementuj taką możliwość poprzez przesłonięcie
# metody __mul__(). Przetestuj działanie.
p1 = Point(2,3)
print(p1)
p2 = p1 * 8
print(p2.x, p2.y)