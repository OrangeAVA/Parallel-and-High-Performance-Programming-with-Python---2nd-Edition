import asyncio

async def f(i):
    print(f'start iteration step {i}')
    await asyncio.sleep(1)
    print(f'end iteration step {i}')
    return i

async def main():
    for coro in asyncio.as_completed([f(i) for i in range(10)]):
        result = await coro
        print('result received:', result)

if __name__ == "__main__":
    asyncio.run(main())
