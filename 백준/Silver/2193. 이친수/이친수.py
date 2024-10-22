import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]


def answer(n):
    if n==1 or n==2:
        return 1
    else:
        dp[1],dp[2] = 1,1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
print(answer(n))