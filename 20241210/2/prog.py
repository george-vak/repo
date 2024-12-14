import asyncio
import random

async def merge(A1, A2, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    if middle < finish:
        await event_in2.wait()

    i, j, k = start, middle, start
    while i < middle and j < finish:
        if A1[i] <= A1[j]:
            A2[k] = A1[i]
            i += 1
        else:
            A2[k] = A1[j]
            j += 1
        k += 1

    while i < middle:
        A2[k] = A1[i]
        i += 1
        k += 1

    while j < finish:
        A2[k] = A1[j]
        j += 1
        k += 1

    event_out.set()

async def mtasks(array):
    n = len(array)
    source, target = array[:], [0] * n
    tasks = []
    events = [asyncio.Event() for _ in range(n)]

    for event in events:
        event.set()

    segment_length = 1
    flip = True

    while segment_length < n:
        new_events = []
        for start in range(0, n, 2 * segment_length):
            middle = min(start + segment_length, n)
            end = min(start + 2 * segment_length, n)
            event_in1 = events[start // segment_length]
            event_in2 = events[middle // segment_length] if middle < n else asyncio.Event()
            event_out = asyncio.Event()
            new_events.append(event_out)

            task = merge(source if flip else target, target if flip else source, start, middle, end, event_in1,
                         event_in2, event_out)
            tasks.append(task)

        events = new_events
        segment_length *= 2
        flip = not flip

    return tasks, source

import sys
exec(sys.stdin.read())
