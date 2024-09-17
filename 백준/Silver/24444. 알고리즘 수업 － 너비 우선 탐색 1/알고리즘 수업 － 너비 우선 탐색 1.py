from collections import deque
import sys
input=  sys.stdin.readline
n,m,r = map(int,input().split())
arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
que = deque()
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for a in arr:
    a.sort()

#print(arr)
#print(visited)
order = 1
que.append(r)
visited[r] = order

while (que):
    next = que.popleft()
    for v in arr[next]:
        if not visited[v]:
            order +=1
            visited[v] = order
            que.append(v)
print(*visited[1:],sep='\n')