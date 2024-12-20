import sys
input = sys.stdin.readline
from itertools import permutations

all_candidate = list(permutations(range(1,10),3))
def check(ques,actual):
    strike,ball = 0,0
    for i in range(3):
        if ques[i] == actual[i]:
            strike +=1
        elif ques[i] in actual:
            ball+=1
    return strike,ball
cnt  =0
n = int(input())
arr =[]
for _ in range(n):
    actual,s,b = map(int,(input().split()))
    actual = tuple(map(int,str(actual)))
    arr.append((actual,s,b))
for actual,s,b in arr:
    all_candidate = [candidate for candidate in all_candidate
    if check(candidate,actual) == (s,b)]
#arr.sort(key = lambda x : x[1],reverse = True) # 스트라이크 많은 순대로 정렬
#print(arr)
print(len(all_candidate))