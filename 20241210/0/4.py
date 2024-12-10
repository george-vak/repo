import asyncio

async def prod(q1):
    for i in range(5):
        await q1.put(i)
        print(f"{prod.__name__} : put {i} to q1")
        await asyncio.sleep(1)
    print(f"{prod.__name__} : stop")

async def mid(q1, q2):
    while True:
        i = await q1.get()
        await q2.put(i)
        print(f"{mid.__name__} : get {i} from q1 and put q2")
        q1.task_done()

async def cons(q2):
    while True:
        i = await q2.get()
        print(f"{cons.__name__} : get {i} from q2")

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    await asyncio.gather(
        prod(q1), mid(q1, q2), cons(q2)
    )

asyncio.run(main())
