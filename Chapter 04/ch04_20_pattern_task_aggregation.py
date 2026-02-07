import asyncio

async def fetch_data(n):
    await asyncio.sleep(0.3)
    print(f"Task {n} completed")
    return n

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print("Aggregate results:", results)

if __name__ == "__main__":
    asyncio.run(main())
