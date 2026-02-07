import asyncio, time

async def other(i, t):
    await asyncio.sleep(t)
    print(f"I am a coroutine {i}")

async def main():
    t1 = time.perf_counter()
    await other(1, 10)
    await other(2, 4)
    await other(3, 3)
    t2 = time.perf_counter()
    print(f"Elapsed time {t2 - t1:.3f} s")

if __name__ == "__main__":
    asyncio.run(main())
