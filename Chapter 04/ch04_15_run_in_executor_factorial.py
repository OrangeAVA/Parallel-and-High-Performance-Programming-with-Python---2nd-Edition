import asyncio
import math

def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, compute_factorial, 10000)
    print("Calculated factorial length:", len(str(result)))

if __name__ == "__main__":
    asyncio.run(main())
