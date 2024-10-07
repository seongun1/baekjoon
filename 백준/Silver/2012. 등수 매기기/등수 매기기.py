import sys
input = sys.stdin.readline

n = int(input())
arr =[int(input()) for _ in range(n)]
rank = [i for i in range(1,n+1)]
arr.sort()
bulman =0
for i in range(n):
    bulman += abs(arr[i] - rank[i])
print(bulman)