import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
dx =[-2,-1,1,2,2,1,-1,-2] #12시부터 시계방향으로
dy =[1,2,2,1,-1,-2,-2,-1]

def find_answer():

    m = int(input())
    arr= [[0 for _ in range(m)] for _ in range(m)]
    s_x,s_y = map(int,input().split())
    t_x,t_y = map(int,input().split())
    visited= [[False for _ in range(m)] for _ in range(m)]

    def in_range(a,b):
        return 0<= a < m and 0<= b <m

    que = deque()
    count =0
    que.append([count,t_x,t_y])
    visited[t_x][t_y] = True
    answer =0
    if t_x == s_x and t_y == s_y:
        return 0
    while que:
        num1 = len(que)
        for _ in range(num1):
            answer,x,y = que.popleft()
            if x == s_x and y == s_y:
                return answer +1
            for i in range(8):
                nx,ny = x+dx[i],y+dy[i]
                if in_range(nx,ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([count,nx,ny])
        count +=1
for _ in range(n):
    print(find_answer())