import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
pool = []
for _ in range(N):
    pool.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
baby_shark_size = 2
baby_shark_stomach = 0
x, y = 0, 0

# 상어 위치
for i in range(N):
    for j in range(N):
        if pool[i][j] == 9:
            x=i
            y=j

def baby_shark_algo(x, y, baby_shark_size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []
    while q:
        tx, ty = q.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if pool[nx][ny] <= baby_shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[tx][ty] + 1
                    if pool[nx][ny] < baby_shark_size and pool[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    return sorted(temp,key=lambda x: (-x[2],-x[0],-x[1]))


cnt =0
result =0
while True:
    shark = baby_shark_algo(x,y,baby_shark_size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(shark) == 0:
        break
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영해준다.
    nx,ny,dist =shark.pop()
    
    #움직이는 칸수가 곧 시간이 된다.
    result += dist
    pool[x][y],pool[nx][ny] = 0,0
    #상어좌표를 먹은 물고기 좌표로 옮겨준다.
    x,y = nx,ny
    cnt += 1
    if cnt == baby_shark_size:
        baby_shark_size += 1
        cnt = 0
print(result)