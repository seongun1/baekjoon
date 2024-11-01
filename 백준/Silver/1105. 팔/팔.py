import sys
input = sys.stdin.readline

a,b = map(str,input().split())
count =0
if len(a) == len(b):
    for x,y in zip(a,b):
        if x=='8' and y =='8':
            count +=1
        elif x !=y:
            break
print(count)