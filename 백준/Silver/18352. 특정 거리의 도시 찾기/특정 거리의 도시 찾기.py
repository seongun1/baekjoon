## 복복습

import sys
from collections import deque

n,m,k,x = map(int,sys.stdin.readline().strip().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,sys.stdin.readline().strip().split())
    adj[s].append(e)

que = deque()

dis = 1
distance = [list() for _ in range(n+1)]
visited = [False] * (n+1)
visited[x] = True

if k==0:
    print(x)
    sys.exit()

for city in adj[x]:
    if not visited[city]:
        distance[1].append(city)
        visited[city] =True
        que.append((city , dis))

while que:
    start, dis = que.popleft()
    if dis >= k:
        continue
    for city in adj[start]:
        if not visited[city]:
            que.append((city,dis +1 ))
            visited[city] = True
            distance[dis+1].append(city)

ans = distance[k]
ans.sort()
if ans:
    for a in ans:
        print(a)
else:
    print(-1)