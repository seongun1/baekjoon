import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 초기화
MAXSIZE = -1
answer = [[MAXSIZE] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 목표 지점 찾기
def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j
    return None

# BFS 거리 찾기
def find_distance():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    start = find_start()
    if not start:
        return  # 시작 지점이 없을 경우

    sx, sy = start
    queue = deque([(sx, sy)])
    answer[sx][sy] = 0
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                answer[nx][ny] = answer[x][y] + 1
                queue.append((nx, ny))

# 모든 0은 0으로 초기화
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer[i][j] = 0

find_distance()

# 출력
for row in answer:
    print(' '.join(map(str, row)))
