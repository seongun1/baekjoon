import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr_n = set()
for _ in range(n):
    arr_n.add(input().rstrip())

count =0
for _ in range(m):
    tmp = input().rstrip()
    if tmp in arr_n:
        count +=1
print(count)