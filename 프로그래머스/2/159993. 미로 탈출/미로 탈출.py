from collections import deque

def find_the_way(maps,start,end):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    arr = deque()
    flag = False
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == start:
                arr.append((i,j,0))
                flag = True
                visited[i][j] = True
                break
        if flag:
            break
    
    while (arr):
        point_x,point_y,count =arr.popleft()
        if maps[point_x][point_y] == end:
            return count
        for x,y in zip(dx,dy):
            nx,ny = point_x+x,point_y+y
            if in_range(nx,ny,maps) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                arr.append((nx,ny,count+1))
                visited[nx][ny] = True
    return -1
def in_range(nx,ny,maps):
    return 0<=nx<len(maps) and 0<=ny<len(maps[0])
    
def solution(maps):
    way_s2l = find_the_way(maps,'S','L')
    way_l2e = find_the_way(maps,'L','E')
    
    if way_s2l != -1 and way_l2e != -1:
        return way_s2l + way_l2e
    else:
        return -1

    


