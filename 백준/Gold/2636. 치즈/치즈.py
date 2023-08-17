import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) #세로의 길이 N 가로의 길이 M
dx = [0,0,1,-1]#상 하 좌 우 
dy = [1,-1,0,0]
cheese = []
graph = [list(map(int,input().split()))for i in range(N)]
def find_melt_cheese():
    visited = [[False] * (M+1) for _ in range(N+1)]
    que = deque()
    que.append([0,0])
    visited[0][0] =True
    cnt =0
    while que:
        y,x= que.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0 <=ny < N and 0<=nx < M :
                if graph[ny][nx] ==0 and visited[ny][nx] == False:
                    que.append([ny,nx])
                    visited[ny][nx] = True
                elif graph[ny][nx] ==1:
                    graph[ny][nx] =0
                    cnt +=1
                    visited[ny][nx] =True
    cheese.append(cnt)
    return cnt
time =0
while True :
    time +=1
    cnt =find_melt_cheese()
    if cnt ==0:
        break
print (time-1)
print(cheese[-2])

        