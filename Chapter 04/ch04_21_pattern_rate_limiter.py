import asyncio, random

async def fetch_data(n, limiter):
    async with limiter:
        await asyncio.sleep(random.uniform(0.1, 0.4))
        print(f"Task {n} completed")
        return n

async def main():
    rate_limiter = asyncio.Semaphore(3)
    tasks = [fetch_data(i, rate_limiter) for i in range(10)]
    results = await asyncio.gather(*tasks)
    print("Results with rate limiting:", results)

if __name__ == "__main__":
    asyncio.run(main())
