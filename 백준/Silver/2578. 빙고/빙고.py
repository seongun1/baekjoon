import sys
input = sys.stdin.readline

arr = [list(map(int,input().split()))for _ in range(5)]
numbers = [tuple(map(int,input().split())) for _ in range(5)]
bingo = [ list(False for _ in range(5))  for _ in range(5)]
#print(bingo)
#print(arr,numbers)
ans =0
def check_vertical(i,j): #수직 빙고 조사
    for k in range(5):
        if not bingo[k][j]:
            return False
    return True
def check_horizon(i,j): #수평 빙고 조사
    for k in range(5):
        if not bingo[i][k]:
            return False
    return True

def check_cross1():
    for k in range(5):
        if not bingo[k][k]:
            return False
    return True
def check_cross2():
    for k in range(5):
        if not bingo[k][4-k]:
            return False
    return True
count =0
for num in numbers:
    for n in num:
        ans +=1
        for i in range(5):
            for j in range(5):
                if arr[i][j] == n:
                    #print(i,j,count)
                    bingo[i][j] = True #빙고판에 체크
                #빙고가 존재하는지 체크(수직, 수평)
                    if check_horizon(i,j):
                        count +=1
                    if check_vertical(i,j):
                        count +=1
                    #대각선의 조건일 경우
                    if i+j ==4 and check_cross2():
                        count +=1
                    if i ==j and check_cross1():
                        count +=1
                if count >=3:
                    print(ans)
                    sys.exit()