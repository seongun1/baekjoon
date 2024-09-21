import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
m = int(input())
computer = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer =0
for _ in range(m):
    a,b = map(int,input().split())
    computer[a].append(b)
    computer[b].append(a)
#print(computer)

que = deque()
que.append(1)
while que:
    #print(que)
    virus = que.popleft()
    for a in computer[virus]:
        if not visited[a]:
            visited[a] = True
            que.append(a)

for count in visited[2:]:
    if count:
        answer +=1
#print(visited)
print(answer)
