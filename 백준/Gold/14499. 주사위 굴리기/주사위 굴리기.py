import sys
input =sys.stdin.readline

n,m,x,y,k = map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(n)]
#동1 서2 북3 남4
dir = list(map(int,input().split()))

dice = [0] *6 #위 / 바닥 / 북 / 남 / 동 / 서
old_dice = dice[:]
old_x,old_y =x,y
for i,dire in enumerate(dir):
    #이전상태 저장
    old_dice = dice[:]
    old_x,old_y = x,y

    if dire == 1: #동
        dice[0],dice[1],dice[4],dice[5] = dice[5],dice[4],dice[0],dice[1]
        y = y+1
    elif dire ==2:#서
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[5],dice[1],dice[0]
        y = y-1
    elif dire == 3: #북
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[2],dice[0],dice[1]
        x= x-1
    elif dire == 4:#남
        dice[0],dice[1],dice[2],dice[3] = dice[2],dice[3],dice[1],dice[0]
        x = x+1

    if not (0<=x<n and 0<=y<m): #만약 지도 바깥으로 가는 경우 롤백
        x,y =old_x,old_y
        dice = old_dice[:]
        continue
    old_x,old_y = x,y
    old_dice = dice[:]
    if arr[x][y] == 0: #이동한 칸의 수가 0이면 바닥면의 수가 칸에 복사
        arr[x][y] = dice[1]
    else:
        dice[1] = arr[x][y]
        arr[x][y] = 0
    print(dice[0])