import asyncio

async def main():
    print('Awaiting for ...')
    await asyncio.sleep(1)
    print('... AsyncIO!')

if __name__ == "__main__":
    asyncio.run(main())
