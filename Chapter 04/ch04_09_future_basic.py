import asyncio

async def get_result(future: asyncio.Future):
    await asyncio.sleep(2)
    future.set_result('...a future result')

async def main():
    my_future = asyncio.Future()
    task = asyncio.create_task(get_result(my_future))
    await task
    print("I'm waiting for ...")
    print(await my_future)
    print('Before continuing with my execution')

if __name__ == "__main__":
    asyncio.run(main())
