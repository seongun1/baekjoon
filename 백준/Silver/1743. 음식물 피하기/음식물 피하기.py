import sys
from collections import deque

input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = [[0] *(m+1) for _ in range(n+1)]
visited = [[False] *(m+1) for _ in range(n+1)]
dx =[0,0,1,-1]
dy = [1,-1,0,0]

#print(arr)
def in_range(x,y):
    return 0<x<=n and 0<y<=m
for _ in range(k):
    r,c = map(int,input().split())
    arr[r][c] = 1
#print(arr)
max_cnt =0
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt =1
            que = deque()
            que.append((i,j))
            while(que):
                x,y = que.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if in_range(nx,ny) and not visited[nx][ny] and arr[nx][ny] == 1:
                        visited[nx][ny] = True
                        cnt +=1
                        que.append((nx,ny))
            max_cnt = max(cnt,max_cnt)
#print(visited)
print(max_cnt)