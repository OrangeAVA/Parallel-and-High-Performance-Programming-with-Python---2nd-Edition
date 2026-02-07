import asyncio, random

async def producer(queue, n):
    for _ in range(n):
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.2)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        await asyncio.sleep(0.3)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    num_items = 5
    prod = asyncio.create_task(producer(queue, num_items))
    cons = asyncio.create_task(consumer(queue))
    await prod
    await queue.join()
    cons.cancel()

if __name__ == "__main__":
    asyncio.run(main())
