import sys
input = sys.stdin.readline
from collections import deque
arr = deque()

arr =[deque(input().strip()) for _ in range(4)]

#print(arr)
k = int(input())


def rotate_clockwise(arr):
    tmp = arr.copy()
    a = tmp.pop()
    tmp.appendleft(a)
    return tmp

def rotate_unclockwise(arr):
    tmp = arr.copy()
    a = tmp.popleft()
    tmp.append(a)
    return tmp

rotate= [] #몇번 톱니바퀴를 어느 방향(1,-1)으로 회전시켰는지
for _ in range(k):
    num,dire = map(int,input().split())

    dir = [0] *4
    index = num -1
    dir[index] = dire

    #오른쪽으로 퍼짐
    for idx in range(index,3):
        if arr[idx][2] == arr[idx+1][-2]:
            break
        #print('--',dir[idx+1], dir[idx])
        dir[idx+1] = -dir[idx]

    #왼쪽으로 퍼짐
    for idx in range(index,0,-1):
        if arr[idx][-2] == arr[idx-1][2]:
            break
        dir[idx-1] = -dir[idx]

    #print(dir)

    for num,rotate in enumerate(dir):
        if rotate ==1:
            arr[num] = rotate_clockwise(arr[num])
        elif rotate == -1:
            arr[num] = rotate_unclockwise(arr[num])
#점수 계산
ans =0
score = 1 #점수
for i in arr:
    ans += score *  int(i[0])
    score *=2
print(ans)  