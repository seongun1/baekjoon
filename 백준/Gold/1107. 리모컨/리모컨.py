import sys
input = sys.stdin.readline

n = int(input()) # 이동하려고 하는 채널
m = int(input()) # 고장난 버튼의 개수
if m:
    broken = list(map(str,input().split()))
else:
    broken = []
remote = [i for i in range(10)]

standard = abs(n-100) # 최댓값

for num in range(1000001):
    for j in str(num):
        if j in broken:
            break
    else:
        standard = min(standard,len(str(num)) + abs(num - n))
print(standard)