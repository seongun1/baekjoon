import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))
#print(arr)
#print('--')
#1. 산술평균
if (sum(arr) /n) <=-1:
    print(f"{sum(arr) / n:.0f}")
else:
    print(abs(int(f"{sum(arr) / n:.0f}")))

#2. 중앙값
arr1 = sorted(arr)
print(arr1[n//2])

#3. 최빈값 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값 출력
arr2 = Counter(arr)
max_val = max(arr2.values())
#print(arr2)
candidate = list(key for key,value in arr2.items() if max_val == value)
candidate.sort()
if len(candidate) >1: #최빈값이 여러개일 경우
    print(candidate[1])
else:
    print(candidate[0])
#4. 범위
print(max(arr) - min(arr))