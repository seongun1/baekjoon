import sys
input = sys.stdin.readline

n,m = map(int,input().split())
sub =[]
ans = [1] *(n+1)
for _ in range(m):
    sub.append(list(map(int,input().split())))
sub.sort()
for a,b in sub:
    if ans[b] <= ans[a]:
        ans[b] = ans[a] +1
print(' '.join(map(str,ans[1:])))