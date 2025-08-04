import sys
input = sys.stdin.readline


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

tetromino =[[(0,0),(0,1),(0,2),(0,3)],
            [(0,0),(0,1),(1,0),(1,1)],
            [(0,0),(1,0),(2,0),(2,1)],
            [(0,0),(1,0),(1,1),(2,1)],
            [(0,0),(0,1),(0,2),(1,1)]]

#모든 방향에 대해 외전
max_ans =0

#print(arr)
def in_range(x,y):
    global n,m
    return 0<=x<n and 0<=y<m

def rotate(arr):
    tmp =[]
    for x,y in arr:
        tmp.append((y,-x))
    return tmp

def flip_ver(arr):
    tmp = []
    for x,y in arr:
        tmp.append((-x,y))
    return tmp

def normalize(arr):
    min_x = min([x for x,y in arr])
    min_y = min([y for x,y in arr])
    return tuple(sorted((x - min_x ,y - min_y) for x,y in arr))
 
all_shapes = set()
for t in tetromino:
    tmp = t.copy()
    for _ in range(4):
        all_shapes.add(normalize(tmp))
        all_shapes.add(normalize(flip_ver(tmp)))
        tmp = rotate(tmp)
#print(len(all_shapes))
#각 도형을 19가지 방향에 대해서 조사
for i in range(n):
    for j in range(m):
        for shape in all_shapes:
            ans =0
            flag = True
            for dx,dy in shape:
                x,y = i+dx,j+dy
                if not in_range(x,y):
                    flag = False
                    break
                ans += arr[x][y]
            if flag:
                max_ans = max(ans,max_ans)
print(max_ans)
