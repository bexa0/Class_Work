from math import pi
class D:
    @staticmethod
    def rectangle(d = 10, h = 1):
        a = pi * d * 2 / 4
        b = pi * d * h
        return round(a * 2 + b, 2)

    def __init__(self, di = 1, hi = 3):
        self.dia = di
        self.h = hi
        self.area = self.rectangle(di,hi)



a = D(1, 2)
print(a.rectangle(2, 2))
x = setattr(a, '2', '3')
print(x)