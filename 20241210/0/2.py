import asyncio

async def squarer(val):
    return val ** 2

async def doubler(val):
    return 2 * val

async def main(x, y):
    numbers = [x, y]
    sqr = await asyncio.gather(*(squarer(num) for num in numbers))
    res = await asyncio.gather(*(doubler(num) for num in sqr))
    print(res)

asyncio.run(main(2, 3))

