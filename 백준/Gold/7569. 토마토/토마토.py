import sys
input = sys.stdin.readline
from collections import deque
m,n,h = map(int,input().split())

arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
#print(arr)
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def in_range(f,x,y):
    return 0<=x<n and 0<=y<m and 0<=f<h

def check_tomato(n,m,h):
    for f in range(h):
        for i in range(n):
            for j in range(m):
                if arr[f][i][j] ==0:
                    return False
    return True

def tomato(n,m,h):
    que = deque()
    for f in range(h):
        for i in range(n):
            for j in range(m):
                if arr[f][i][j] == 1:
                    que.append((f,i,j))
    days = 0
    while (que): #토마토 익힘 처리
        for _ in range(len(que)):
            f,x,y = que.popleft()
            #print(f"{f} ,, {x} ,, {y}")
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if in_range(f,nx,ny) and arr[f][nx][ny] == 0:
                    arr[f][nx][ny] = 1
                    que.append((f,nx,ny))
            for p in range(-1,2,2):
                if in_range(f+p,x,y) and arr[f+p][x][y] ==0:
                    arr[f+p][x][y] =1
                    que.append((f+p,x,y))
        days +=1
    
    if not check_tomato(n,m,h):
        return -1

    return days -1
ans = tomato(n,m,h)
print(ans)