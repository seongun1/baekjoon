import sys
from itertools import combinations
input= sys.stdin.readline
moem_alpabet = ['a','e','i','o','u']

L,C = map(int,input().split()) #L개의 알파벳 소문자들로 구성 . 암호로 사용했을 법한 문자의 종류 C가지
password = input().split()
password.sort()
words= list(combinations(password,L))
answer =[]
#모든 조합 중에서, 최소 한개 모음과 최소 두개 자음이 포함되어 있는 경우만 추가한다.
for i in words:
    #password의 조합 중 하나하나를 체크
    jaem =0
    moem =0
    for alpabet in i:
        #그 하나하나 중 알파벳 하나씩을 체크
        if alpabet in moem_alpabet:
            moem +=1
        else:
            jaem +=1
    if moem >=1 and jaem >=2:
        print(''.join(list(i)))