import sys
input = sys.stdin.readline

n,k = map(int,input().split())
count =0
arr = [[0 for _ in range(k+1)] for _ in range(n+1)]
#print(arr)
for i in range(k+1):
    arr[0][i] =1
for i in range(n+1):
    arr[i][1] =1
for i in range(1,n+1):
    for j in range(2,k+1):
        arr[i][j] = sum(row[j-1] for row in arr[:i+1])
#print(arr)
print(arr[n][k] % 10**9)