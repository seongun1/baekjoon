import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split()) #세로길이 N , 가로길이 M 
answer = 0
if N == 1:
    answer = 1
elif N ==2:
    if M <= 6:
        answer = (M+1) //2
    elif M >= 7:
        answer = 4
elif N >= 3:
    if M <=6:
        answer = min(M,4)
    elif M >=7:
        answer = M-2
print(answer)
