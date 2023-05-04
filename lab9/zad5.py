class Point:
    def __init__(self,x=0 , y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point({self.x},{self.y}) '
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    def __eq__(self, other):
        if isinstance(other, Point) == True:
            return self.x == other.x and self.y == other.y
        else:
            return False

class other2:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
class Polygon:
    def __init__(self):
        self.points = []
    def add_point(self, point):
        self.points.append(point)
        return f'Point {self.points} '


#Zadanie 5
#Stwórz klasę o nazwie Polygon i zdefiniuj właściwość
# points typu list, która będzie docelowo przechowywała obiekty typu
# Point. Inicjalizuj pustą listę w konstruktorze. Zdefiniuj również metodę
# add_point(point: Point), która będzie dodawała punkt do listy.
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)

print(polygon.points)
