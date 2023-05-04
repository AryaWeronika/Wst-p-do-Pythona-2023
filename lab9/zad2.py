#Zadanie 1
#Zadeklaruj klasę Point o właściwościach x oraz y
# (oba typ int). Obie właściwości powinny posiadać domyślną wartość równą zero
# (wywołanie konstruktora bez podania wartości inicjalizujących).
class Point:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point({self.x},{self.y}) '
#Zadanie 2
#Przesłoń w klasie Point metodę __str__() tak, aby zwracała tekst Point(x, y)
# gdzie x i y przedstawia aktualną wartość tych właściwości.
p1 = Point(1,2)
print(p1)