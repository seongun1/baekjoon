import sys
input = sys.stdin.readline

n,m = map(int,input().split())
sub =[]
ans = [1] *(n)
for _ in range(m):
    sub.append(list(map(int,input().split())))
sub.sort()
for a,b in sub:
    if ans[b-1] <= ans[a-1]:
        ans[b-1] = ans[a-1] +1
print(' '.join(map(str,ans)))