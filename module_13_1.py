# Домашнее задание по теме "Асинхронность на практике"

import asyncio


async def start_strongman(name, power):
    shars = 5
    speed = 10/power
    print(f'Силач {name} начал соревнования.')
    for i in range(1,shars+1):
        await asyncio.sleep(speed)
        print(f'Силач {name} поднял {i} шар')
        if i == 5:
            print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha',3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apolon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())