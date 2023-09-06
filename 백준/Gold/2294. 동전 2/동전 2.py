import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    tmp = int(input())
    coin.append(tmp)

dp = [0] * (k + 1)
dp[0] = 0  # 0원을 만들기 위한 최소 동전 개수는 0개

for i in range(1, k + 1):
    dp[i] = float('inf')  # 무한대로 초기화

for c in coin:
    for i in range(c, k + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == float('inf'):
    print(-1)  # 만들 수 없는 경우
else:
    print(dp[k])  # 최소 동전 개수 출력
