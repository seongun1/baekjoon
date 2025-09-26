import sys
input = sys.stdin.readline

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

if len(str1) < len(str2):
    str1,str2 = str2,str1

dp = [[0] *len(str1) for _ in range(len(str2))]
answer=0

for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            if i ==0 or j ==0:
                dp[i][j] =1
            else:
                dp[i][j] = dp[i-1][j-1]+1
            answer = max(answer,dp[i][j])
print(answer)