# from internet
import numpy as np


def snake(n):
    MAXINDEX = n - 1
    VECT = np.array([[-1, 1], [0, 1], [1, -1], [1, 0]])  # Вектор изменения индекса
    matr = np.zeros((n, n), dtype=int)  # Первоначальная матрица - нулевая
    iVect = 0  # Индекс текущего направления
    spos = np.array([0, 0])  # Текущая позиция
    for i in range(1, n ** 2 + 1):
        matr[tuple(spos)] = i
        if min(spos) == MAXINDEX:  # Дошли до конца
            return matr
        elif spos[n % 2] == 0:  # Перед следующим условием из-за диагонали
            iVect += 1
        elif max(spos) == MAXINDEX:  # Дошли до максимального элемента - повернули назад
            iVect -= 1
        elif min(spos) == 0:  # Дошли до нулевого - повернули вперед
            iVect += 1
        spos += VECT[iVect % 4]  # Цикличность индекса


print('snake(4)=\n', snake(4))
print('snake(5)=\n', snake(5))

n = int(input())


def put(x, r):
    global v, k
    for i in range(0, len(x)):
        if r == 1:
            i = len(x) - i - 1
        v[x[i]].append(k)
        k = k + 1


v = [[] for i in range(n)]
x = [0]
k = 1

for i in range(n):
    put(x, (i + 1) % 2)
    x.append(x[len(x) - 1] + 1)
x.pop()
for i in range(n):
    del (x[0])
    put(x, (i + (n + 1) % 2) % 2)

for i in v:
    print(i)