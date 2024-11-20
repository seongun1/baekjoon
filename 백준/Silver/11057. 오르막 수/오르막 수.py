import sys
input = sys.stdin.readline

n = int(input())
cnt=0
dp =list([1] *(10) for _ in range(n+1))
#print(dp)
if n>1:
    for k in range(2,n+1):
        dp[k][0] = sum(dp[k-1])
        for i in range(1,10):
            tmp =0
            for j in range(i):
                tmp += dp[k-1][j]
            dp[k][i] = dp[k][0] - tmp
            #print(f"{dp[k][i]} = {dp[k][0]} - {tmp}")       
print(sum(dp[n])%10007)