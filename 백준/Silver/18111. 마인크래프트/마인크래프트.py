import sys
from collections import Counter
input = sys.stdin.readline

n,m,b = map(int,input().split())
arr =[]
#print(arr)
for _ in range(n):
    arr.extend(map(int,input().split()))

#print(arr)

max_height = max(arr)
min_height = min(arr)

land = Counter(arr)
min_time = sys.maxsize
ans_height = 0
for target_height in range(min_height,max_height+1):
    spare_block = b
    time = 0
    for height,blocks in land.items():
        if target_height < height: #블록을 깎아야 함.
            time += 2*blocks *(height - target_height)
            spare_block += blocks  * (height - target_height)
        elif target_height > height: #블록을 추가해야 함
            time +=  blocks * (target_height - height)
            spare_block -= blocks * (target_height - height)
    if spare_block <0:
        continue
    if min_time > time or (min_time == time and ans_height < target_height):
        min_time = time
        ans_height = target_height
print(min_time, ans_height)
