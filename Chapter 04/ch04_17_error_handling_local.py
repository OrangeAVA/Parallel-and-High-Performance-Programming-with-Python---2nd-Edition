import asyncio

async def fetch_data(n):
    try:
        if n == 3:
            raise ValueError("Error in task 3")
        await asyncio.sleep(1)
        print(f"Task {n} completed successfully")
    except ValueError as e:
        print(f"Error caught: {e}")

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
