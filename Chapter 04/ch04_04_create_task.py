import asyncio

async def other():
    print("I am a coroutine")

async def main():
    task = asyncio.create_task(other())
    print('Awaiting for ...')
    await asyncio.sleep(1)
    await task
    print('... AsyncIO!')

if __name__ == "__main__":
    asyncio.run(main())
