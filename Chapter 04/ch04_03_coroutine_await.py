import asyncio

async def other():
    print("I am a coroutine")

async def main():
    print('Awaiting for ...')
    await asyncio.sleep(1)
    await other()
    print('... AsyncIO!')

if __name__ == "__main__":
    asyncio.run(main())
