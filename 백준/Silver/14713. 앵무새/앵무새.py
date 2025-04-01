# 앵무새가 말하는 문장들은 전부 모든 문장들의 첫 번째가 다 나가야 한다.
# 따라서 possible 리스트에 각각의 제일 왼쪽의 단어들을 담아 두고,
# 만약 말하는 문장을 단어 단위로 쪼개서 그 possible 리스트 안에 있으면, 계속 진행하고
# 그렇지 않으면 Impossible을 출력한다.

import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
#print(n)
arr =[]
for _ in range(n):
    arr.append(deque(map(str,input().split())))

sentence = list(input().split())

def print_answer(sentence):
    
    for s in sentence: # flag 대신에 for-else 문을 활용용
        for candidate in arr:
            if len(candidate) >0 and s == candidate[0]:
                #print(candidate[0])
                candidate.popleft()
                flag = True
                break
        else:
            return "Impossible"
        
    #단어를 다 적었는데 앵무새가 말한 단어가 남아 있다면 -1
    if any(candidate for candidate in arr):
        return "Impossible"
    return "Possible"
print(print_answer(sentence))