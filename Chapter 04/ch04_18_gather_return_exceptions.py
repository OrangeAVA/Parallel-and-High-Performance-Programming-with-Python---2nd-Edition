import asyncio

async def fetch_data(n):
    if n == 2:
        raise ValueError("Error in task 2")
    await asyncio.sleep(1)
    return f"Task {n} completed"

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} generated an error: {result}")
        else:
            print(f"Task result {i}: {result}")

if __name__ == "__main__":
    asyncio.run(main())
