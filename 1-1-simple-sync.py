# 1-1-simple-sync.py

#Task A: Computer 0 + 1
#Time: 0.00
#Task A: Computer 1 + 2
#Time: 0.00
#Task A: Sum = 3
#
#Task B: Computer 0 + 1
#Time: 0.00
#Task B: Computer 1 + 2
#Time: 0.00
#Task B: Computer 3 + 3
#Time: 0.00
#Task B: Sum = 6
#
#Time: 0.01 sec

import time

def sleep(): #กำหนดดีเลย์หรือหน่วงเวลา
    print(f'Time: {time.time() - start:.2f}')
    time.sleep

# Function sum the data in task
def sum(name, numbers):
    total = 0 #ตั้งค่า0
    for number in numbers: #ลูปนำค่าในtaskนั้นๆมาคำนวณทั้งหมด
        print(f'Task {name}: Computer {total} + {number}')
        sleep()
        total += number
    # Show total of task
    print(f'Task {name}: Sum = {total}\n')

start = time.time() #เริ่มนับเวลา
# Summation the total in that turn of each team and show running time (float 2 digit)
tasks = [ #เก็บค่าในแต่ละตัวแปรและเรียกใช้คำสั่ง
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time() #สิ้นสุดการนับเวลา
print(f'Time: {end-start:.2f} sec') #แสดงเวลาที่ใช้ทั้งหมด