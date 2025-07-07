from collections import deque
def solution(land):
    answer = 0
    col = len(land)
    row = len(land[0])
    land_per_row = [0] *(row)
    
    visited= [[False] *row for _ in range(col)]
    
    def dfs(x,y):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        que = deque()
        que.append((x,y))
        count =0
        visited[x][y] = True
        arr =set()
        arr.add(y)
        while (que):
            count +=1
            cur_x,cur_y = que.popleft()
            for i in range(4): #현재위치에서 상하좌우만큼 탐색
                nx,ny = cur_x + dx[i],cur_y + dy[i]
                if (0<=nx <col and 0<=ny < row) and not visited[nx][ny] and land[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny] = True
                    arr.add(ny)
        return count,arr
    for y in range(row):
        oil = 0
        for x in range(col):
            if not visited[x][y] and land[x][y]:
                oil,arr= dfs(x,y)
                for a in arr:
                    land_per_row[a] += oil
    
    return max(land_per_row)