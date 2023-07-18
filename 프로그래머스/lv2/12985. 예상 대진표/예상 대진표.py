import math

def solution(n,a,b):
    answer = 1
    n =math.log(n,2)
    a1 = math.ceil(a/2)
    b1 = math.ceil(b/2)
    if  a1==b1:
        return answer
    while(n!=0): # 최종 한명이 남을때까지 진행
        n-=1
        a = math.ceil (a/2)
        b= math.ceil (b/2)
        if a==b:
            return answer
        answer +=1
        
    return answer
        
        