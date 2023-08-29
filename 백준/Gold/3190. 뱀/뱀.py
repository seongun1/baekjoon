import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) #보드의 크기
k = int(input()) #사과의 개수
board = [[0]*n for _ in range(n)]

dir = dict()
for i in range(k):
    y,x = map(int,input().split())
    board[y-1][x-1] = 1 #사과를 1로 표시
l = int(input()) # 뱀의 방향 전환 정보
for i in range(l):
    x,c = input().split()
    dir[int(x)] =c

deq = deque()
y,x = 0,0
deq.append([y,x])

board[y][x] =2 #뱀의 머리를 2로 설정
direction =0

def turn (L):
    global direction
    if L == 'D':
        direction = (direction +1) %4
    else:
        direction = (direction -1) %4

dx = [1,0,-1,0]
dy = [0,1,0,-1] # 오 아래 왼 위
time =0
while (1):
    time +=1
    y += dy[direction]
    x += dx[direction]
    # 벽에 닿으면 게임 종료
    if x <0 or x >=n or y<0 or y>=n:
        break
    if board[y][x] ==1: # 사과가 있다면
        board[y][x] =2
        deq.append([y,x])
        if time in dir:
            turn(dir[time])
    elif board[y][x] ==0: #사과가 없다면?
        board[y][x] =2
        deq.append([y,x])
        ty,tx = deq.popleft()
        board[ty][tx] =0
        if time in dir:
            turn(dir[time])
    else:
        break
print(time) 

