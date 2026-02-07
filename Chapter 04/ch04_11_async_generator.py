import asyncio

async def gen(n):
    for i in range(n):
        await asyncio.sleep(0.2)
        yield i

async def main():
    async for i in gen(10):
        print(i)

if __name__ == "__main__":
    asyncio.run(main())
