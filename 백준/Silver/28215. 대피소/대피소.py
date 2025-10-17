from itertools import combinations
import sys

n,k = map(int,sys.stdin.readline().strip().split())

arr = [list(map(int,input().split())) for _ in range(n)]
shelter = list(combinations(arr,k))

min_ans = 10**6
distance =[]
for s in shelter:
    tmp =[]
    for a in arr:
        x,y = a[0], a[1]
        min_dis = min_ans
        for i in range((len(s))):
            s_x,s_y = s[i][0] , s[i][1]
            dis = abs(s_x - x) + abs(s_y - y)
            min_dis = min(min_dis , dis)
        tmp.append(min_dis)
    distance.append(max(tmp))
print(min(distance))