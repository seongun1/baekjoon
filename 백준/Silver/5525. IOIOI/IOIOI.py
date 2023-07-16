import sys
input = sys.stdin.readline

N = int(input())
M = int(input()) #S의 길이 M
S = input() #입력 받는 문자열 M
pointer =0
answer =0
count = 0
while pointer < M-1: # 문자열 끝까지 가면 종료
    #IOI라는 하나의 블럭을 담는 과정. N이 1이면 IOI는 하나이고, 
    # N이 2이면 IOIOI니깐 IOI라는 블럭은 두개이다.(예제에서 세는 방식이 그렇다)
    if S[pointer : pointer +3]== "IOI":
        count +=1
        pointer +=2
        if count ==N:
            answer +=1
            count -=1
    else:
        pointer += 1
        count =0

print(answer)