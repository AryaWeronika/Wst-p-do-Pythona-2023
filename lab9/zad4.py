class Point:
    def __init__(self,x=0, y=0):
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


#Zadanie 4
#Przesłoń w klasie Point metodę __eq__() odpowiedzialną za porównywanie tego
# obiektu (self) z innym (other) w sensie tożsamości. Wartość True zwracana jest
# tylko wtedy, gdy jest to dokładnie ten sam typ obiektu (czyli Point) oraz wartości
# x i y są identyczne dla obu obiektów.
#p1 = Point(2,3)
#print(p1)
#p2 = p1 * 8
#print(p2.x, p2.y)
#print(type(Point))
#print(isinstance( Point, type))
p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(4, 5)

print(p1 == p2)  # True
print(p1 == p3)  #False