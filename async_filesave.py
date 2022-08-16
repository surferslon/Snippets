import asyncio
import aiohttp  # pip install aiohttp

def write_image(data):  # bad idea to use sync code with async
    filename = 'file-{}.jpg'.format(int(time() * 1000)
    with open(filename, 'wb) as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)

async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch_content(url, session)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())