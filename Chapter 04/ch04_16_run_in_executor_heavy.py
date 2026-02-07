import asyncio
import time

def heavy_computation(n):
    start = time.time()
    s = 0
    for i in range(n):
        s += i * i
    end = time.time()
    print(f"Computation took {end - start:.2f} seconds")
    return s

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, heavy_computation, 10**7)
    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
