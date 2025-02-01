import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
import copy

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
wall_candiate= []
virus = []
def print_arr(arr1):
    for a in arr1:
        for b in a:
            print(b, end =' ')
        print()
    print()
def in_range(x,y):
    return 0<=x<n and 0<=y<m

#벽 세우기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            wall_candiate.append((i,j))
        elif arr[i][j] == 2:
            virus.append((i,j))

wall = list(combinations(wall_candiate,3))
max_ans =0
for a,b,c in wall:
    arr_tmp = copy.deepcopy(arr) #arr 의 값이 바뀌게 되므로, deepcopy를 해줘야 함함
    arr_tmp[a[0]][a[1]] =1
    arr_tmp[b[0]][b[1]] =1
    arr_tmp[c[0]][c[1]] =1
    que = deque(virus)
    while(que):
        x,y = que.popleft()
        #print(x,y)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if in_range(nx,ny) and arr_tmp[nx][ny] == 0:
                que.append((nx,ny))
                arr_tmp[nx][ny] = 2
                
    #print_arr(arr_tmp)
    ans =0
    for i in range(n):
        for j in range(m):
            if arr_tmp[i][j] == 0:
                ans +=1
    max_ans = max(ans,max_ans)
print(max_ans)
