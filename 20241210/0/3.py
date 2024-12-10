import asyncio

async def wait(name, ev, evname):
    await ev.wait()
    print(f"{name} : {evname}")

async def send(name, ev, evname):
    ev.set()
    print(f"{name} generated {evname}")

async def snd(ev):
    await send("snd", ev, "ev")

async def mid(num, evw, evs):
    await wait(f"mid{num}", evw, "evsnd")
    await send(f"mid{num}", evs, f"evmid{num}")

async def rcv(ev0, ev1):
    await wait("rcv", ev0, "ev0")
    await wait("rcv", ev1, "ev1")


async def main():
    evs, evm0, evm1 = asyncio.Event(), asyncio.Event(), asyncio.Event()
    res = await asyncio.gather(rcv(evm0, evm1),
                               mid(1, evs, evm1), mid(0, evs, evm0), snd(evs)
    )
    return res

asyncio.run(main())

