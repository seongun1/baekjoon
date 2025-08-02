import sys
input =sys.stdin.readline
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

time =0

n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
#print(arr)
#outside_list = [(0,0)]
#outside_arr 초기화

def find_outside(): #외부와 맞닿아 있는 부분을 찾기
    visited = [[False]*m for _ in range(n)] #외부와 연결되어 있는 부분을 찾는 배열
    outside = deque()
    outside.append((0,0))
    while outside:
        x,y = outside.popleft()
        for i in range(4):
            nx,ny = x+dx[i] , y+dy[i]
            if 0<=nx<n and 0<=ny<m and (nx,ny) and not visited[nx][ny] and not arr[nx][ny]:
                visited[nx][ny] = True
                outside.append((nx,ny))
    return visited

def print_arr(arr):
    for a in arr:
        for i in a:
            print(i, end=' ')
        print()

# def melting_cheese():
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == -1: #지움 마킹된 치즈
#                 outside_list.append((i,j))
#                 arr[i][j] = 0
while (1):
    time +=1
    outside = find_outside()
    #print_arr(outside)
    melt_list = []
    #한 시간만에 녹아 없어지는 치즈를 찾기
    for i in range(n):
        for j in range(m):
            if arr[i][j]: #치즈를 검사
                count =0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx < n and 0<=ny < m and outside[nx][ny]:
                        count +=1
                    if count >=2 : #카운트가 2 이상일 경우 -> 치즈를 없앰
                        melt_list.append((i,j))
                        break
    #print(melt_list)
    if not melt_list:
        print(time-1)
        break
    for x,y in melt_list:
        arr[x][y] = 0

    # print()
    # print_arr(arr)
    # print("time=" , time)
    # #melting_cheese()
