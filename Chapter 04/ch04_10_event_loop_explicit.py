import asyncio

async def main():
    print('Starting...')
    await asyncio.sleep(3)
    print('...Ending')

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
