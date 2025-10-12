import sys

d,n = map(int,sys.stdin.readline().split())
oven = list(map(int,sys.stdin.readline().split()))

pizza = list(map(int,sys.stdin.readline().split()))

ans = [0] * len(pizza)

for i in range(1,len(oven)):
    oven[i] = min(oven[i-1],oven[i])

bottom = len(oven)-1
#print(oven)
for p in pizza:
    flag = False
    for i in range(bottom,-1,-1):
        #print(p,i,oven[i])
        if oven[i] >= p:
            bottom = i-1
            flag = True
            break
    if not flag:
        bottom = 0
        break

print(bottom +2) if flag else print(max(bottom,0))