import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

length = min(len(s1) , len(s2))
dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]


dp[0][0] = 1 if s1[0] == s2[0] else 0

for j in range(1, len(s2)): #첫 행 확인
    if s1[0] == s2[j]:
        dp[0][j] = max(1, dp[0][j-1])
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1,len(s1)): #첫 열 확인
    if s1[i] == s2[0]:
        dp[i][0] = max(1,dp[i-1][0])
    else:
        dp[i][0] = dp[i-1][0]

for i in range(1,len(s1)):
    for j in range(1,len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = max(dp[i-1][j-1] +1, dp[i-1][j] , dp[i][j-1])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j],dp[i-1][j-1])

print(dp[-1][-1])