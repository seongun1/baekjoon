import sys
sys = sys.stdin.readline

n = int(input())
friends = [list(map(str,input().rstrip())) for _ in range(n)]

connect =[[0]*n for _ in range(n)]

#플로이드 워셜 알고리즘 - 무엇을 거쳐갈 알고리즘을 판단할 때

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if friends[i][j] == 'Y' or (friends[i][k] == 'Y' and friends[k][j] == 'Y'):
                connect[i][j] = 1
ans = 0
#print(friends)
#print(connect)
for c in connect:
    ans = max(ans,sum(c))
print(ans)