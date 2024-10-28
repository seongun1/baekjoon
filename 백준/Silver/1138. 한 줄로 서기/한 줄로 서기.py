import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = [n+1 for _ in range(n)]
for i,a in enumerate(arr):
    count=0
    for j in range(n):
        if ans[j] == n+1:
            count +=1
            if count >a:
                ans[j] = i+1
                break
            
print(*ans)