import numpy as np


# datal = [6, 7.5 , 5, 8, 0, 1]
# arl = np.array(datal)
# print(arl)


# one = [1, 2, 3]
# two = [4, 5, 6]
# three = [7, 8, 9]
# a = np.array([one, two, three])
# print(a)


# arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# print(arr)

# task1
r = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]
a = np.array(r)
print(a[:,0])

# task2
b = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]
a = np.array(b)
print(a[0], a[3])

# task3
c = [h for h in np.arange(0, 10) if h % 2 == 0]
print(c)

l = [h for h in np.arange(0, 100) if h % 3 == 0 and h % 7 == 1]
print(l)

# task 4
matrix = [
    [10, 200, 3, 5],
    [8, 2, 3, 1],
    [0, 20, 7, -1]
]
cols = list(
    list(row[i] for row in matrix) for (i, e) in enumerate(matrix[0]) if i % 2 and matrix[len(matrix) - 1][i] < e)
print(cols)