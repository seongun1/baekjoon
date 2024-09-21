import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
arr = []
for _ in range(m):
    arr.append(list(map(int,input().split())))
#print(arr)
friends =[[] for _ in range(n+1)]
visited =[False for _ in range(n+1)]
for a,b in arr:
    friends[a].append(b)
    friends[b].append(a)
#print(friend)
que = deque()
answer = []
que.append(1)
visited[1] = True
level =0
while que and level < 2:
    frined_number = len(que)
    for _ in range(frined_number):
        friend= que.popleft()
        for a in friends[friend]:
            if not visited[a]:
                visited[a] = True
                answer.append(a)
                que.append(a)
    
    level +=1
print(len(answer))

