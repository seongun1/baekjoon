from collections import deque
def solution(land):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    answer = 0
    n,m = len(land),len(land[0])
    arr =[] #석유가 묻어져 있는 좌표
    visited = [[False for _ in range(m)] for _ in range(n)]
    def bfs(i,j):
        cols_oil = set()
        n,m = len(land),len(land[0])
        val =1
        que =deque()
        que.append((i,j))
        while que:
            x,y = que.popleft()
            visited[x][y] = True
            cols_oil.add(y)
            for k in range(4):
                nx,ny = x + dx[k], y + dy[k]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx,ny))
                    val +=1
        return val,list(cols_oil)
    #석유 지도를 만듦
    cols_oil = [0] * m
    for i in range(n):
        ans = 0
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                ans , cols = bfs(i,j)
                for c in cols:
                    cols_oil[c] += ans
    return max(cols_oil)