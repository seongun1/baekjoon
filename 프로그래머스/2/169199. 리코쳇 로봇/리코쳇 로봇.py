from collections import deque

def in_range(board,x,y):
    return 0<=x<len(board) and 0<=y<len(board[0])

def find_start(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                return i,j   
def solution(board):
    arr= deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0] #오른 / 왼 / 아래 / 위
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    #시작점 설정
    start_x,start_y = find_start(board)
    
    def bfs(x,y,dir):
        while(1):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if not in_range(board,nx,ny):
                break
            elif board[nx][ny] == 'D':
                break
            x,y = nx,ny
        x,y = nx-dx[dir],ny-dy[dir]
        return x,y
    arr.append([start_x,start_y,0]) # 시작점, 거리
    while(arr):
        x,y,dis = arr.popleft()
        #print(x,y,dis)
        for i in range(4):
            nx,ny = bfs(x,y,i)
            if visited[nx][ny]:
                continue
            elif board[nx][ny] == 'G':
                return dis+1
            else:
                arr.append([nx,ny,dis+1])
                visited[nx][ny] = True
    return -1