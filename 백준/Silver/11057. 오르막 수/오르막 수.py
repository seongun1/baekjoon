import sys
input = sys.stdin.readline

n = int(input())
dp =list([1] *(10) for _ in range(n+1))
#print(dp)
#dp[k][i] = 자릿수가 k 번째인 수에서, 마지막 자릿수가 i일때 가능한 경우의 수.
for k in range(2,n+1):
    dp[k][0] = dp[k-1][0]
    for i in range(1,10):
        dp[k][i] = (dp[k-1][i] + dp[k][i-1]) % 10007
print(sum(dp[n]) % 10007)