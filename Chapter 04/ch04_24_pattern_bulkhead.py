import asyncio

async def limited_task(n, limiter, section_name):
    async with limiter:
        await asyncio.sleep(0.2)
        print(f"Task {n} completed in section {section_name}")

async def main():
    limiter_a = asyncio.Semaphore(2)
    limiter_b = asyncio.Semaphore(3)
    tasks = [limited_task(i, limiter_a, 'A') for i in range(5)] + \            [limited_task(i, limiter_b, 'B') for i in range(5, 10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
