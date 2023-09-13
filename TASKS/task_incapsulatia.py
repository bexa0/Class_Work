class A:
    # property
    name = 'Mirsaid'

    # method set
    def set_value(self, attr, value):
        self.__setattr__(attr, value)

    #method get
    def get_value(self, attr):
        self.__getattribute__(attr)

    # another method __setattr__
    def __setattr__(self, attr, value):
        if attr == 'name':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + 'критическая ошибка')

    def __getattribute__(self, attr):
        if attr == 'name':
            return object.__getattribute__(self, attr)


a = A()
print(f'name {a.name}')
a.name = 'Blabla'
print(f"name {a.name}")