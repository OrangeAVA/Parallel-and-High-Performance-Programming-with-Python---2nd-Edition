# NOTE: Requires 'aiohttp' and internet access to run.
# pip install aiohttp
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        await response.text()
        print(f"Completed: {url}")

async def main():
    urls = ["http://example.com" for _ in range(20)]  # reduce for demo
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
