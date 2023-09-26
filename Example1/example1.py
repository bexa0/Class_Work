print(10)
print(20)
print(30)

print(40)

class Device:
    def __init__(self, mark):
        self.mark = mark
        self.device = 'Home device'
        self.volt = '220V'


class CoffeeMachine(Device):
    def __init__(self, mark, color):
        super().__init__(mark)
        self.color = color

    def get_info(self):
        print('CoffeeMachine')
        print(self.device, self.volt, self.mark, self.color)

class Blender(Device):
    def __init__(self, mark, speed):
        super().__init__(mark)
        self.speed = speed

    def get_info1(self):
        print('Blender')
        print(self.device, self.volt, self.mark, self.speed)


class MeatGrinder(Device):
    def __init__(self, mark, blade):
        super().__init__(mark)
        self.blade = blade

    def get_info2(self):
        print('Blender')
        print(self.device, self.volt, self.mark, self.blade)


get = CoffeeMachine('Bosh', 'black')
get1 = Blender('Bosh', 2)
get2 = MeatGrinder('Bosh', 'Cross')

choice = input('1. CoffeeMachine\n2. Blender\n3. MeatGrinder\nChoice: ')

if choice == '1':
    get.get_info()
elif choice == '2':
    get1.get_info1()
elif choice == '3':
    get2.get_info2()
else:
    print('Something go wrong.')
