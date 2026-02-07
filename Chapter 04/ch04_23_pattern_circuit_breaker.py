import asyncio

class CircuitBreaker:
    def __init__(self, max_failures, reset_timeout):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failures = 0
        self.open = False

    async def call(self, func, *args):
        if self.open:
            print("Open circuit, attempt refused.")
            return
        try:
            result = await func(*args)
            self.failures = 0
            return result
        except Exception as e:
            self.failures += 1
            print(f"Error: {e}, failed attempts: {self.failures}")
            if self.failures >= self.max_failures:
                self.open = True
                print("Open circuit, waiting for reset.")
                await asyncio.sleep(self.reset_timeout)
                self.failures = 0
                self.open = False

async def unstable_task(n):
    if n % 2 == 0:
        raise ValueError("Simulated Error")
    await asyncio.sleep(0.1)
    return f"Task {n} completed"

async def main():
    cb = CircuitBreaker(max_failures=2, reset_timeout=1)
    tasks = [cb.call(unstable_task, i) for i in range(6)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
