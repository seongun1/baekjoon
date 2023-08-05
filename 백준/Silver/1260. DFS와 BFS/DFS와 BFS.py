import sys
input = sys.stdin.readline
sys.setrecursionlimit (10 **9)
from collections import deque

N,M,V = map(int,input().split()) #정점의 갯수 /간선의 갯수/ 탐색을 시작할 정점의 번호 
tree=[[]for _ in range (N+1)]
for i in range(M):
    a,b= map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)


# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고 를 충족.
for i in tree:
    i.sort()
def DFS(V):
    visited[V] = True
    print(V,end =" ")
    for i in tree[V]:
        if not visited[i]:
            DFS(i)


def BFS(V):
    que = deque([V])
    visited[V] = True
    while que:
        start =que.popleft()
        print(start,end =" ")
        for i in tree[start]:
            if not visited[i]:
                visited[i] = True
                que.append(i)

#DFS
visited= [False] * (N+1)
DFS(V)
print()

#BFS
visited = [False] *(N+1)
BFS(V)

