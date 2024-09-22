import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr =[list(map(int,list(input().strip()))) for _ in range(n)]
#print(arr)

def in_range(n,m,a,b):
    return 0 <= a < n and 0 <= b <m
ans =1
line = len(arr[0]) if len(arr) > len(arr[0]) else len(arr)
#print(line)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        target = arr[i][j]
        for k in range(1,line):
            if in_range(n,m,i+k,j+k) and arr[i][j+k] == target and arr[i+k][j] == target and arr[i+k][j+k] == target:
                #print(i,j,'====')
                ans = max(k+1,ans)
print(ans**2)