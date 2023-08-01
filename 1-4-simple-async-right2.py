#Task A: Computing 0+1
#Time: 0.00
#Task B: Computing 0+1
#Time: 0.01
#Task A: Computing 1+2
#Time: 1.00
#Task B: Computing 1+2
#Time: 1.01
#Task A: Sum = 3
#
#Task B: Computing 3+3
#Time: 2.03
#Task B: Sum = 6
#
#Time: 3.05 sec

import asyncio
import time
# Make synchronous sleep
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)
# Define sum
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
# Change the synchronous function
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3])) #ฟังก์ชันกำหนดการทำงานต่อเนื่องแบบจัดลำดับแน่นอน
# Call function running process
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

