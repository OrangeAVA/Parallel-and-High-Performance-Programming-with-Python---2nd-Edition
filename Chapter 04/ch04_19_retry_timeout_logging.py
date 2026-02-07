import asyncio, random, logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_data_with_retry(n, retries=3, delay=0.5):
    for attempt in range(retries):
        try:
            if random.random() < 0.5:
                raise ValueError(f"Temporary error in task {n}")
            await asyncio.sleep(0.3)
            logging.info(f"Task {n} successfully completed on attempt {attempt + 1}")
            return f"Result of task {n}"
        except ValueError as e:
            logging.warning(f"Attempt {attempt + 1} for task {n} failed: {e}")
            await asyncio.sleep(delay)
    raise RuntimeError(f"Task {n} failed after {retries} attempts")

async def fetch_data(n):
    await asyncio.sleep(n * 0.2)
    return f"Task {n} completed"

async def main():
    # Retry demo
    tasks = [fetch_data_with_retry(i) for i in range(5)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    logging.info(f"Results: {results}")
    # Timeout demo
    timed = [asyncio.wait_for(fetch_data(i), timeout=0.5) for i in range(5)]
    results2 = await asyncio.gather(*timed, return_exceptions=True)
    for i, r in enumerate(results2):
        if isinstance(r, asyncio.TimeoutError):
            logging.error(f"Task {i} expired")
        else:
            logging.info(f"Task result {i}: {r}")

if __name__ == "__main__":
    asyncio.run(main())
