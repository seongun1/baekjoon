import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

# 그래프 인접 리스트 생성
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

# 최단 거리 저장 리스트 (모든 도시까지의 거리 초기화)
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시의 거리는 0

# BFS 탐색 시작
que = deque([x])
while que:
    start = que.popleft()
    for next_city in arr[start]:
        if distance[next_city] == -1:  # 아직 방문하지 않은 도시라면
            distance[next_city] = distance[start] + 1
            que.append(next_city)

# 정답 출력 (거리가 정확히 k인 도시들)
ans = [i for i in range(1, n + 1) if distance[i] == k]

if ans:
    print(*ans, sep='\n')
else:
    print(-1)
