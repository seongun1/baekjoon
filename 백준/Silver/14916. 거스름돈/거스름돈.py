import sys

n = int(input())
dp = [100000 for _ in range(n+1)] 
if n >=5:
    dp[5] = 1
    dp[2] = 1
    dp[4] = 2
elif n >=4:
    dp[2] = 1
    dp[4] = 2
elif n>=2:
    dp[2] = 1
else:
    dp[1] = -1

for i in range(6,n+1):
    dp[i] = min(dp[i-2]+1,dp[i-5]+1)
#print(dp[1:])
if dp[n] >= 100000:
    print(-1)
else:
    print(dp[n])