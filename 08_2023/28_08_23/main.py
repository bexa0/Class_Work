import numpy as np
import random

# mass2 = np.array([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
# print(mass2)

# mass3 = np.arange(1,100)
# print(mass3)

# a = np.arange(0, 100, 5)
# a.shape = (4, 5)
# print(a)

# r = np.zeros(4)
# print(r)

# r = np.ones(4)
# print(r)

# r = np.array([random.randint(-10, 10) for x in range(0, 10)])
# print(r)

# temp = np.array(([random.randint(-10, 10) for i in range(0, 10)]))
# temp.shape = (2, 5)
# print(temp)


#task1
r = np.zeros(10)
print(r)

p = np.arange(0,10, 2)
print(p)

a = np.arange(0, 10, 3)
print(list(reversed(a)))

found = [0, 1 , 2, 'x']
for i in found:
    if i == "x":
        found = True
        print(found)


# b = [x for x in np.arange(0, 10) if x % 2 == 0]
# print(b)

v = [i for i in np.arange(0, 100) if i % 3 == 0 and i % 7 == 1]
print(v)