import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]
#print(arr)

def cal_distance(x1,y1,x2,y2):
    return abs(x1- x2) + abs(y1 - y2)

chicken =[]
home =[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append((i,j))
#print(home,chicken)
can_chicken = list(combinations(chicken,m))
#print(home)
min_distance =sys.maxsize
for a in can_chicken:
    min_dis =0
    #print(a)
    for x1,y1 in home:
        dis = sys.maxsize
        for x2,y2 in a:
            if dis > cal_distance(x1,y1,x2,y2):
                dis = cal_distance(x1,y1,x2,y2)
            #print(x1,y1,x2,y2)
        #print(dis)
        min_dis += dis
    min_distance = min(min_dis,min_distance)
print(min_distance)