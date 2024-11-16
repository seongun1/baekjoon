import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
#print(arr)
MAXSIZE = -1
answer = [[MAXSIZE] *m for _ in range(n)]
visited =  [[False] *m for _ in range(n)]
#print(answer)

#목표 지점 찾기
def find_start():
    for i in range(n):
        for j in range(m):
            if arr[i][j] ==2:
                return i,j
def print_arr(map_arr):
    for row in map_arr:
       print(' '.join(map(str,row)))

# print(find_start())
#print_arr(arr)
# print_arr(answer)
# print(visited)
# 목표 지점 - 원하는 지점까지의 거리 구하기
# 목표 지점으로부터 dfs를 활용해, 덱에 거리를 넣는다. 
def find_distance(n,m):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def in_range(x,y):
        return 0<=x<n and 0<=y<m

    target_x,target_y = find_start() #목표지점
    #print(target_x,target_y,'++')

    visited[target_x][target_y] = True
    que = deque([(target_x,target_y)])
    answer[target_x][target_y] = 0

    while (que):
        #print(que)
        x,y= que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if in_range(nx,ny) and not visited[nx][ny] and arr[nx][ny] != 0 :
                answer[nx][ny] = answer[x][y]+1
                visited[nx][ny] = True
                que.append([nx,ny])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer[i][j] = 0
find_distance(n,m)
print_arr(answer)