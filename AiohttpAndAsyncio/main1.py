# from random import randint
# import asyncio
#
# a = None
# event = asyncio.Event()
#
# async def fun_a():
#     global a
#     while True:
#         a = randint(0,99)
#         event.set()
#         await asyncio.sleep(2)
#
# async def fun_b():
#     while True:
#         await event.wait()
#         print('New number is: ', a)
#         event.clear()
#
# if __name__ == '__main__':
#     event_loop = asyncio.get_event_loop()
#     event_loop.create_task(fun_a())
#     event_loop.create_task(fun_b())
#     event_loop.run_forever()


#TASK1 выводит рандомные числа
# from random import randint
# import asyncio
#
# a = None
# event = asyncio.Event()
#
# async def fun_a():
#     global a
#     while True:
#         a = randint(0,99)
#         event.set()
#         await asyncio.sleep(2)
#
# async def fun_b():
#     while True:
#         await event.wait()
#         print('New numbe name is: ', a)
#         event.clear()
#
# if __name__ == '__main__':
#     event_loop = asyncio.get_event_loop()
#     event_loop.create_task(fun_a())
#     event_loop.create_task(fun_b())
#     event_loop.run_forever()


#TASK2 выводит имена рандомно
# import random
# import asyncio
#
# n = ['Dljkds', 'nsdkjfhkjsdf', 'jdsfkjsdhf']
#
# a = None
# event = asyncio.Event()
#
# async def fun_a():
#     global a
#     while True:
#         a = random.choice(n)
#         event.set()
#         await asyncio.sleep(2)
#
# async def fun_b():
#     while True:
#         await event.wait()
#         print('New numbe name is: ', a)
#         event.clear()
#
# if __name__ == '__main__':
#     event_loop = asyncio.get_event_loop()
#     event_loop.create_task(fun_a())
#     event_loop.create_task(fun_b())
#     event_loop.run_forever()

# не законченный код
import random
import asyncio
from openpyxl import Workbook

n = ['Dljkds', 'nsdkjfhkjsdf', 'jdsfkjsdhf']

a = None
event = asyncio.Event()

async def fun_a():
    global a
    while True:
        a = random.choice(n)
        event.set()
        await asyncio.sleep(1)

async def fun_b():
    while True:
        await event.wait()
        if a == 3:
            break
        print('New numbe name is: ', a)
        event.clear()

wb = Workbook()
ws = wb.active
ws['A1'] = a
wb.save("sample.xlsx")

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.create_task(fun_a())
    event_loop.create_task(fun_b())
    event_loop.run_forever()