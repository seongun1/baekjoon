from collections import deque


def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    def in_range(x,y):
        return 0<=x<len(maps) and 0<=y<len(maps[0])
    
    def bfs(x,y):
        if maps[x][y] == 'X' or visited[x][y]:
            return 0
        arr = deque()
        arr.appendleft([x,y])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        cnt =0
        while (arr):
            x,y = arr.popleft()
            if visited[x][y]:
                continue
            visited[x][y] =True
            if maps[x][y] != 'X':
                cnt += int(maps[x][y])
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if in_range(nx,ny) and not visited[nx][ny] and maps[x][y] !='X':
                    arr.append([nx,ny])
        return cnt
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            result = bfs(i,j)
            if result >0:
                answer.append(result)
    answer.sort()
    if not answer:
        return [-1]
    return answer