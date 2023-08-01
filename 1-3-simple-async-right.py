#Task A: Computing 0+1
#Time: 0.00
#Task B: Computing 0+1
#Time: 0.00
#Task A: Computing 1+2
#Time: 1.01
#Task B: Computing 1+2
#Time: 1.02
#Task A: Sum = 3
#
#Task B: Computing 3+3
#Time: 2.03
#Task B: Sum = 6
#
#Time: 3.03 sec

import asyncio
import time
# Make synchronous delay in task A to B
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1) #ให้หน่วงเวลามีการทำงานแบบซิงโครนัส
# Function sum and print
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
# get and process the synchronous loop
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
# Finish then print ending process
end = time.time()
print(f'Time: {end-start:.2f} sec')