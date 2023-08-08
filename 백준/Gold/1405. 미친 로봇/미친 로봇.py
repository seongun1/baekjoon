import sys
input = sys.stdin.readline
from collections import deque
#값 입력
tmp = list(map(int,input().split()))
N = tmp[0]
pos = tmp[1:]
for i in range(len(pos)):
    pos[i] = pos[i] * 0.01

dx = [-1,1,0,0] #동 서 남 북
dy = [0,0,-1,1]

def dfs(x,y,visitied,per):
    global ans
    if len(visitied) == N+1:
        ans += per
        return
    for i in range(4):
        nx, ny = x + dx[i] , y + dy[i]
        if [nx,ny] not in visitied:
            visitied.append([nx,ny])
            dfs(nx,ny,visitied,per * pos[i])
            visitied.pop()
       
ans =0
dfs(0,0,[[0,0]],1)
print(ans)  
