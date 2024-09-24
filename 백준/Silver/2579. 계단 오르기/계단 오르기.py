import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]+  [int(input()) for _ in range(n)]
dp  = [0 for _ in range(n+1)]
#print(stairs)
if n <=2:
    dp[n] = sum(stairs)
elif n ==3:
    dp[3] = max(stairs[1],stairs[2]) +stairs[3]
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1],stairs[2]) + stairs[3]
    for i in range(4,n+1):
        dp[i] = max(dp[i-2] +stairs[i],stairs[i] + stairs[i-1] + dp[i-3])

print(dp[n])