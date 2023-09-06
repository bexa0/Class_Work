#defolt method
class Name:
    def student(self, name):
        self.name = name
        print('Hello', name)


a = Name()
a.student('bexa')



# static method
# статический метод нужен для проверки и др.
class Name1:
    @staticmethod
    def student1():
        print('Hello i am student')


Name1.student1()
print()



from math import pi
class Front:
    @staticmethod
    def rectangle(d, h):
        a = pi * d * 2 / 4
        b = pi * d * h
        return round(a * 2 + b, 2)



    def __init__(self, di, hi):
        self.dia = di
        self.h = hi
        self.area = self.rectangle(di,hi)

from datetime import date
a = Front(1, 2)
print(a.rectangle(2, 2))
print(a.area)
print()


# class Person:
#     def __init__(self, name, age):
#         self.name = name,
#         self.age = age
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person = Person("mayank", 21)
# person1 = Person.fromBirthYear('mayank', 1996)
#
# print(person.age)
# print(person1.age)
# print()
# print(Person.isAdult(22))


# class Man:
#     instance_count = 0
#     def __init__(self, name):
#         Man.instance_count += 1
#     @staticmethod
#     def counter():
#         return Man.instance_count
#
#
# a = Man('a')
# b = Man('aa')
# c = Man('fga')
# print(Man.counter())


class Point2D:
    instances_count = 0

    def __init__(self, x, y):
        self.x = x,
        self.y = y
        Point2D.instances_count += 1

    def __str__(self):
        return 'Точка 2D({},{}'.format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point2D(self.x + other.x, self.y + other.y)
        elif isinstance(other,(int, float)):
            self.x += other
            self.y += other
            return self
        else:
            raise TypeError('Не могу добавить{1} к {0}'.
            format(self.__class__, type(other)))

    def __sub__(self, other):
        '''Создать новый объект как разность координат self и other.'''
        return Point2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        '''Вернуть новый объект, инвертировав координаты'''

    def __eq__(self, other):
        '''Вернуть ответ, является ли точки одинаковыми.'''
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not(self == other)

    @staticmethod
    def sum(*points):
        assert len(points) > 0, 'Количество суммируемых точек = 0!'

        res = points[0]
        for point in points[1:]:
            res += point

        return res

    @classmethod
    def from_string(cls, str_value):
        values = [float(x) for x in str_value.split(',')]
        assert len(values) == 2

        return cls(*values)

if __name__ == '__main__':
    p1 = Point2D(0, 5)
    p2 = Point2D(-5, 10)
    p3 = Point2D.from_string('5, 6')

    print(p1 + p3) #Точка 2D(5.0, 11.0)

    print(Point2D. instances_count) # 4(p1, p2, p3, p1 + p2)

    p4 = Point2D.sum(p1, p2, p3, Point2D(0, -21))
    print(p4)