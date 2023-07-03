import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split()) #공간의 크기 N과 M (N은 세로줄의 갯수, M은 가로줄의 갯수)

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,1,1,-1,-1]
index = [list(map(int,input().split())) for i in range (N)]
dq = deque()
for i in range(N):
    for j in range(M):
       if index[i][j] == 1: #상어가 있는 위치라면, dq에 삽입(상어가 있는 위치에서 탐색하기 위함)
           dq.append([i,j])
result = 0
while dq:
    x,y = dq.popleft()
    for a in range (8):
        nx = x + dx[a]
        ny = y + dy[a]
        if nx <0 or ny <0 or nx >= N or ny >= M: #주변 탐색시 범위를 벗어난 경우
            continue
        if index[nx][ny] != 0: #만약 이미 탐색을 마쳤거나 주변탐색 시 상어가 있는 경우
            continue
        dq.append([nx,ny])
        index[nx][ny] = index[x][y] +1
        result = max(result,index[x][y]+1)

print(result -1)