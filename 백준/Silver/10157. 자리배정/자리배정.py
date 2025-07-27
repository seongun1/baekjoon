import sys
input = sys.stdin.readline

m,n = map(int,input().split())
k = int(input())

arr = [[0]*m for _ in range(n)]
#print(arr)
dx = [-1,0,1,0] #위 오른 아래 왼
dy = [0,1,0,-1]

x,y = n-1,0 #왼쪽 아래부터 시작
seat =1
dir =0 #현재 방향
arr[x][y] = seat

if k > n*m:
    print(0)
    sys.exit(0)

while (seat < k): #대기번호 k 인사람이 올떄까지 (대기번호 k까지 채워야함)
    nx,ny = x + dx[dir],y+dy[dir]
    if 0<=nx < n and 0<=ny<m and arr[nx][ny] ==0:
        x,y = nx,ny
    else: #범위가 넘어가면 방향을 바꾼 뒤 다시
        dir = (dir+1) %4
        continue
    seat +=1
    arr[x][y] = seat
    #print('==',ans_x,ans_y,dir,x,y)

def print_arr():
    for a in arr:
        for i in a:
            print(i,end=' ')
        print()
#print_arr()

print(y+1,n-x)