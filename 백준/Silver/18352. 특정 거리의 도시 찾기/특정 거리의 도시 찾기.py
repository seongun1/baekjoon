import sys
from collections import deque
input = sys.stdin.readline
n,m,k,x = map(int,input().split())

arr =[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
#print(arr)

que = deque()
distance = [-1] *(n+1)
#print(visited)
distance[x] = 0
que.append(x)

while (que):
    start = que.popleft()
    for i in arr[start]:
        if distance[i] == -1:
            distance[i] = distance[start] + 1
            que.append(i)

ans = [i for i in range(1,n+1) if distance[i] == k]
ans.sort()
if not ans:
    print(-1)
else:
    print(*ans, sep= '\n')