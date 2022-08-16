# program for counting and showing time every 3 seconds

# event loop:
#   coroutine > Task (Future)



import asyncio


async def print_nums():  # async menas @asyncio.coroutine
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('n seconds', count)
        count += 1
        await asyncio.sleep(1)



async def main():
    task1 = syncio.create_task(print_nums())
    task2 = syncio.create_task(print_time())

    # yeld from asyncio.gather(task1, task2)
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # python 3.7-
    #loop = syncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()
    # python 3.7+
    asyncio.run(main())