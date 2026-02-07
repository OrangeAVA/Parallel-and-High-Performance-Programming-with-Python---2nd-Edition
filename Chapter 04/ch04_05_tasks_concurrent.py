import asyncio, time

async def other(i, t):
    await asyncio.sleep(t)
    print(f"I am a coroutine {i}")

async def main():
    t1 = time.perf_counter()
    task1 = asyncio.create_task(other(1, 10))
    task2 = asyncio.create_task(other(2, 4))
    task3 = asyncio.create_task(other(3, 1))
    await task1
    await task2
    await task3
    t2 = time.perf_counter()
    print(f"Elapsed time {t2 - t1:.3f} s")

if __name__ == "__main__":
    asyncio.run(main())
