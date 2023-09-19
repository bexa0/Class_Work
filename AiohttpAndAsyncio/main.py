import aiohttp
import asyncio

async def func():
    # открытие сесси в aiohttp
    async with aiohttp.ClientSession() as session:
        query = {
            'param' : 'data',
            'param1' : 'data1'
        } #параметры

        #отправляет запрос
        response = await session.get("https://google.com/")
        print(response.text) #текст данных
        print(response.status) #код статуса
        print(response.url) #ссылка
        print(await response.json()) #json формат

loop = asyncio.new_event_loop() #новый асинхронный цыкл
loop.create_task(func()) #добавляект в него новый функцию
loop.run_forever() #запускает цыкл