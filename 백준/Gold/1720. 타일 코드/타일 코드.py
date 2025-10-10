import sys
from itertools import combinations_with_replacement

n = int(sys.stdin.readline())
if n ==1:
    print(1)
    sys.exit()
elif n ==2:
    print(3)
    sys.exit()
    
dp = [0] * (n+1)
t = [0] *(n+1)
s = [0] *(n+1)

dp[1] ,dp[2] = 1,3
t[1],t[2] = 1,3


for i in range(3,n+1):
    if i%2: #홀수
        s[i] = t[(n-1) //2 ]
    else:
        s[i] = t[i//2] + 2*t[i//2 -1]
    t[i] = t[i-1] + 2*t[i-2]

    dp[i] = ( s[i] + t[i] ) /2

print(int(dp[n]))
