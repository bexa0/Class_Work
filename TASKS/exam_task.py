import random

# a = str(input('Введите к, н, б:'))
# list = ['к', 'н', 'б']

# ran = random.choice(list)
# print(ran)


a = str(input('Введите к, н, б:'))

list = ['к', 'н', 'б']
ran = random.choice(list)
# print(ran)

if a != list[0] and a != list[1] and list[2]:
    print('Введи только к, н, б')
    b = str(input('Введите к, н, б:'))

def play():
    if ran == 'к' and a == 'н':
        print(ran)
        print('бот выграл')
    if ran == 'н' and a == 'н':
        print(ran)
        print("Ничья")
    if ran == 'б' and a == 'н':
        print(ran)
        print('Ты выграл')
    if ran == 'к' and a == 'к':
        print(ran)
        print('ничья')
    if ran == 'н' and a == 'к':
        print(ran)
        print('ты выграл')
    if ran == 'б' and a == 'к':
        print(ran)
        print('бот выграл')
    if ran == 'к' and a == 'б':
        print(ran)
        print('ты выграл')
    if ran == 'н' and a == 'б':
        print(ran)
        print('бот выграл')
    if ran == 'б' and a == 'б':
        print(ran)
        print('ничья')
play()

one_more_time = str(input('Хочешь еще раз сыграть (y/n)'))
# if one_more_time == 'y':
#     a = str(input('Введите к, н, б:'))
# if one_more_time == 'n':
#     break


for i in one_more_time:
    if i == 'y':
        a = str(input('Введите к, н, б:'))
        play()
    else:
        print('Спасибо за игру')
        break



# oen_more_time = str(input('Хочешь еще раз сыграть (y/n)'))
# if oen_more_time == 'y':
#     pass