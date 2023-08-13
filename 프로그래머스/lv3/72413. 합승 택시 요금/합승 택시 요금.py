from heapq import heappop,heappush
INF = int(1e9)
graph =[[]]
#다익스트라 알고리즘
def process(n,fares):
    global graph
    graph =[[] for i in range(n+1)]
    #그래프에 간선 정보를 저장
    for fare in fares:
        start,end,cost,=fare[0],fare[1],fare[2]
        graph[start].append([end,cost])
        graph[end].append([start,cost])
def daikstra(start,end):
    global graph
    n= len(graph)
    table = [INF for i in range(n)]
    table[start] =0
    pq =[[0,start]]
    
    while pq:
        w,x = heappop(pq)
        
        if table[x] < w:
            continue
        for item in graph[x]:
            nx,ncost = item[0],item[1]
            ncost += w
            if ncost < table[nx]:
                table[nx] = ncost
                heappush(pq,[ncost,nx])
    return table[end]
def solution(n, s, a, b, fares):
    process(n,fares)
    cost = INF
    
    for i in range(1,n+1):
        cost = min(cost,daikstra(s,i)+daikstra(i,a)+daikstra(i,b))
        
    return cost