import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr= []
for _ in range(n):
    tmp = input().strip()
    arr.append(list(tmp))

visited= [list(False for _ in range(m)) for _ in range(n)]
answer =[]
#처음에 중앙을 찾고, 그 다음 상하좌우 검사 -> 만약 다 있다면, 정답에 추가

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find_cross():
    for x in range(n):
        for y in range(m):
            if arr[x][y] == '*':
                cnt =1
                flag = True
                tmp = []
                while (1):
                    for i in range(4):
                        tmp.append([x,y])
                        nx,ny = x+ dx[i] * cnt , y+dy[i] * cnt
                        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == '*':
                            tmp.append([nx,ny])
                            continue
                        else:
                            flag = False
                            break
                    if flag:
                        #print(x,y,tmp)
                        for a,b in tmp:
                            visited[a][b] = True
                        answer.append([x+1,y+1,cnt])
                        cnt +=1
                        continue
                    else:
                        break
def print_answer():
    flag = True
    for x in range(n):
        for y in range(m):
            if arr[x][y] == '*' and visited[x][y] == False:
                flag = False
                break
        if not flag:
            break
    if not flag or len(answer) ==0:
        print(-1)
        return
    print(len(answer))
    for coord in answer:
        print(*coord)
    return

find_cross()
print_answer()