import sys
input = sys.stdin.readline

t = int(input())
MAX_n = 1000000
dp = [0] * (MAX_n+1)
dp[1],dp[2],dp[3] = 1,2,4
for i in range(4,MAX_n+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009

for _ in range(t):
    n = int(input())
    print(dp[n] % 1000000009)