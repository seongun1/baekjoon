from collections import deque
   
def bfs(h,w):
    answer =0
    arr = []
    for _ in range(h):
        tmp = input()
        arr.append(list(tmp))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    #print(arr)
    #print(len(arr), len(arr[0]),'--------')
    visited = [[False]*w for _ in range(h)]
    #print(len(visited),len(visited[0]),'+++++')
    def in_range(x,y):
        return 0<= x<h and 0<= y<w
    group = deque()
    for i in range(h):
        for j in range(w):
            #print(i,j,'----')
            if visited[i][j]:
                continue
            if arr[i][j] == '#':
                visited[i][j] = True
                group.append([i,j])
                answer +=1
                while(group):
                    x,y = group.popleft()
                    visited[x][y] = True
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if in_range(nx,ny) and not visited[nx][ny] and arr[nx][ny] == '#':
                            visited[nx][ny] = True
                            group.append([nx,ny])
    return answer

t = int(input())
for _ in range(t):
    h,w = map(int,input().split())
    print(bfs(h,w))