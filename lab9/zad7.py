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
    def __str__(self):
        points_str = ", ".join(str(p) for p in self.points)
        return f"Polygon[{points_str}]"
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return self.points[item]
        else:
            raise TypeError("Invalid argument type for __getitem__(), expected int or slice")


#Zadanie 7
#W klasie Polygon przesłoń metodę __getitem__(), tak aby możliwe było zwrócenie
# pojedynczego punktu (item to int) oraz wycinka (item to slice). W tej metodzie obsłuż
# wyjątek TypeError jeżeli nie jest to int lub slice.
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)
p4 = Point(4, 4)
p5 = Point(5, 5)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)
polygon.add_point(p4)
polygon.add_point(p5)

# pobranie pojedynczego punktu z listy
print(polygon[0])  # wypisze: Point(1, 1)

# pobranie wycinka listy
sub_polygon = polygon[1:4]
print(sub_polygon)