import sys
input= sys.stdin.readline
from collections import deque
n = int(input())
arr=  [list(map(int,input().split())) for _ in range(n)]

def find_max():
    # max_val = 0
    # for a in arr:
    #     tmp = max(a)
    #     max_val = max(tmp,max_val)
    # return max_val
    return max(map(max,arr)) #--> 간결하게 개선
def print_arr(arr):
    for a in arr:
        for i in a:
            print(i,end=' ')
        print()
max_val = find_max()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def safe_area(rained):
    n = len(rained)
    visited=[[False] *n for _ in range(n)]
    # print_arr(rained)
    ans =0
    for i in range(n):
        for j in range(n):
            if not rained[i][j] and not visited[i][j]: #방문하지 않은 지역과 잠기지 않은 지역
                # print(i,j,'++++')
                ans +=1
                visited[i][j] = True
                que = deque()
                que.append((i,j))
                while(que):
                    x,y = que.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k],y+dy[k]
                        if  (0<= nx <n and 0<= ny <n) and not visited[nx][ny] and not rained[nx][ny]:
                            visited[nx][ny] = True
                            que.append((nx,ny))
    # print('___________')    
    # print_arr(visited)
    # print('___________')    
    return ans


# print(arr)
# print(max_val)
# print(is_rained)
max_ans = 1
for rain in range(1,max_val+1):
    rained = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= rain:
                rained[i][j] = True
    max_ans = max(safe_area(rained),max_ans)
print(max_ans)