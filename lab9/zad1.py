#Zadanie 1
#Zadeklaruj klasę Point o właściwościach x oraz y
# (oba typ int). Obie właściwości powinny posiadać domyślną wartość równą zero
# (wywołanie konstruktora bez podania wartości inicjalizujących).
class Point:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y
