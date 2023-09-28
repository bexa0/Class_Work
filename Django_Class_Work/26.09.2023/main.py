import random
# def task1():
#     list1 = [1, 2, 3, 4, 5]
#     b = ['-{}+'.format(number) for number in list1]
#     print(b)
# task1()

# def task2():
#     slovar = {'a' : 1, 'b' : 2, 'c' : 3}
#     a = dict(reversed(slovar.items()))
#     print(a)
# task2()

def task3():
    text = 'Hi, my name is Ben'
    x = ' '.join(text)
    y = ['{}!'.format(i) for i in text]
    print(x)
    print(y)
task3()



# def task6():
#     b = random.randint(0, 15)
#     print('Угадай число\nУ тебя есть три попытки')
#     user = input()
#     i = 0
#     while i < 3:
#         if b < user:
#             print('Меньше')
#             i += 1
#         if b > user:
#             print('Больше')
#         if b == user:
#             print('Ты угадал')
#
#
# task6()