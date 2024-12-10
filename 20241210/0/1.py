import asyncio
import time
from idlelib.window import add_windows_to_menu


async def late(sec):
    s = time.strftime('%X')
    await asyncio.sleep(sec)
    return sec, s, time.strftime('%X')

async def main():
    print(*await asyncio.gather(
        late(1), late(2), late(3), late(4)
    ))
    # print(*(await late(1)))
    # print(*(await late(2)))
    # task3 = asyncio.create_task(late(3))
    # task4 = asyncio.create_task(late(4))
    # print(*(await task3))
    # print(*(await task4))



asyncio.run(main())
