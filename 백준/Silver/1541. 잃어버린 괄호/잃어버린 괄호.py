import sys
input = sys.stdin.readline

s = 0
arr = input().split('-')
#print(arr)
#print(arr[0])
for i in arr[0].split('+'):
    s +=int(i)

for k in arr[1:]:
    for j in k.split('+'):
        #print(k.split('+'),'----',j)
        s -= int(j)
print(s)