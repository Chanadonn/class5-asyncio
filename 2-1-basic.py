#Wed Jul 26 15:39:48 2023 hello 1 started
#Wed Jul 26 15:39:48 2023 hello 2 started
#Wed Jul 26 15:39:52 2023 hello 1 done
#Wed Jul 26 15:39:52 2023 hello 2 done
#Time: 4.02 sec

import asyncio
import time
# Make reply noti function
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")
# Create task
async def main():
    task1 = asyncio.create_task(hello(1)) #returns immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2
# Run all process
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')