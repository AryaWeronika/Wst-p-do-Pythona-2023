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


#Zadanie 6
#W klasie Polygon przesłoń metodę __str__() tak, aby wypisanie
# Polygon wyglądało mniej więcej tak: Polygon[Point(2, 3), Point(1,1), ...].
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)

polygon = Polygon()
polygon.add_point(p1)
polygon.add_point(p2)
polygon.add_point(p3)

#print(polygon.points)
print(polygon)