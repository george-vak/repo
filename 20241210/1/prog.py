import asyncio
from asyncio import Queue

ev = asyncio.Event()

async def stacker(queue, stack):
    while not ev.is_set():
        item = await queue.get()
        await stack.put(item)

async def reader(stack, count, delay):
    for i in range(count):
        await asyncio.sleep(delay)
        item = await stack.get()
        print(item)
    ev.set()

async def writer(queue, delay):
    counter = 0
    while not ev.is_set():
        await asyncio.sleep(delay)
        await queue.put(f"{counter}_{delay}")
        counter += 1


async def main(queue, stack, delay1, delay2, delay3, count):
    tasks = [
    reader(stack, count, delay3),
    writer(queue, delay1),
    writer(queue, delay2),
    stacker(queue, stack)
    ]
    await asyncio.gather(*tasks)


delay1, delay2, delay3, count = eval(input())
stack = Queue()
queue = Queue()

asyncio.run(main(queue, stack, delay1, delay2, delay3, count))
