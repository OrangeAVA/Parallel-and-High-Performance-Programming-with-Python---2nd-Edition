import asyncio

async def coroutine(t, id):
    await asyncio.sleep(t)
    print(f"I am the coroutine {id}")
    return t + 2

async def main():
    results = await asyncio.gather(
        coroutine(10, "A"),
        coroutine(4, "B"),
        coroutine(2, "C"),
    )
    print("The results are:", results)

if __name__ == "__main__":
    asyncio.run(main())
