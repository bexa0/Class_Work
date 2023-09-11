# class A:
#     def person(self):
#         print('Hello my name is David')
#
# b = A()
# b.__person__()

class A:
    def __init__(self):
        self.age = 0

    def get_number_age(self):
        print('this is get_number_age')
        return self._age

    def set_number_age(self, a):
        print('This is set_number_age')
        self._age = a

    def t_age(self):
        del self._age

    age = property(get_number_age, set_number_age)


a = A()
a.age = 10
print(a.age)