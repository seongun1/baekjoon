import sys

input = sys.stdin.readline

n = int(input())
num = int(input())

arr = [[0] * n for _ in range(n)]

dx = [-1,0,1,0] # 위 오른 아래 왼
dy = [0,1,0,-1]
ans_x,ans_y = 0,0

def check(x,y,n):
    return 0<=x<n and 0<=y<n

def print_arr(n,num):
    global ans_x,ans_y
    count =2
    stack =1
    dir =0 #방향
    x,y = n//2, n//2
    arr[x][y] = 1

    if num ==1:
        ans_x,ans_y = x+1, y+1

    while (1):
        for _ in range(2):
            for _ in range(stack):
                if count > n*n:
                    return
                nx,ny = x+dx[dir],y+dy[dir]
                arr[nx][ny] = count
                if count == num:
                    ans_x,ans_y = nx+1,ny+1 
                count +=1
                x,y = nx,ny
            dir = (dir + 1) % 4
        stack += 1

print_arr(n,num)
for a in arr:
    print(*a)

print(ans_x,ans_y)