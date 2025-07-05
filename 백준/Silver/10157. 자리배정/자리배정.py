import sys
input = sys.stdin.readline

c,r = map(int,input().split()) #가로 / 세로
arr =[[None] * c for _ in range(r)]
dx = [-1,0,1,0] #위 -> 오른 -> 아래 -> 왼
dy = [0,1,0,-1]
k = int(input())
nx = [0,1,0,-1]
ny = [1,0,-1,0]

dir =0
count =1

cur_row,cur_col = r-1 ,0
ans_x,ans_y = 1,1
arr[cur_row][cur_col] = (ans_x,ans_y)

def print_arr():
    for a in arr:
        for i in a:
            print(i,end =' ')
        print()

if r*c < k:
    print(0)
    exit()

for _ in range(1,k):
    next_row ,next_col = cur_row + dx[dir] , cur_col + dy[dir]

    #만약 arr을 넘어가면, 방향 전환
    if not (0<= next_row < r and  0<=next_col< c) or arr[next_row][next_col] is not None:
        dir = (dir +1) %4
        next_row ,next_col = cur_row + dx[dir] , cur_col + dy[dir]

    arr[next_row][next_col] = (ans_x + nx[dir] , ans_y + ny[dir])
    cur_row ,cur_col = next_row, next_col
    ans_x += nx[dir]
    ans_y += ny[dir]

#print_arr()
print(ans_x,ans_y)