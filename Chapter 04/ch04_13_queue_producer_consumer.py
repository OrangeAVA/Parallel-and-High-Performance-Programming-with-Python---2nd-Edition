import asyncio
import random

async def producer(name, queue):
    n = random.randint(0, 5)
    await asyncio.sleep(n)
    await queue.put(n)
    print(f"Producer {name} adds {n} to the queue")

async def consumer(name, queue):
    while True:
        n = await queue.get()
        await asyncio.sleep(n)
        print(f"Consumer {name} receives {n} from the queue")
        queue.task_done()

async def main(nproducers=4, nconsumers=2):
    q = asyncio.Queue()
    producers = [asyncio.create_task(producer(n, q)) for n in range(nproducers)]
    consumers = [asyncio.create_task(consumer(n, q)) for n in range(nconsumers)]
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    asyncio.run(main())
