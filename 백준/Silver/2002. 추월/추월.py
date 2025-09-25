import sys
input = sys.stdin.readline

n = int(input())
car_in =[input().strip() for _ in range(n)]
car_out = [input().strip() for _ in range(n)]

count = 0
cars ={}
for i,car in enumerate(car_in):
    cars[car] = i+1

arr=[]
for c in car_out:
    arr.append(cars[c])

ans =0

#추월 판정
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            ans +=1
            break
print(ans)