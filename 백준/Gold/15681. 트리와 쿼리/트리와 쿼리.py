import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 **9)

n,r,q = map(int,input().split()) # 정점의 수 / 루트의 번호 / 쿼리의 수
tree = [[]for _ in range(n+1)]
graph = [0] * (n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def checkpoint (x):
    graph[x] =1
    for i in tree[x]:
        if not graph[i]>0:
            checkpoint(i)
            graph[x] += graph[i]

checkpoint(r)

for i in range(q):
    u = int(input())
    print(graph[u])