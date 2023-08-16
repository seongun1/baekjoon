from itertools import combinations
from bisect import bisect_left

def solution(info,query):
    answer =[]
    dict = {}
    for i in range(len(info)):
        infol = info[i].split()
        jogun = infol[:-1]
        jumsu = int(infol[-1])

        for j in range(5): # key로 만드는 조합 생성
            for c in combinations(jogun,j):
                tmp = ''.join(c)
                if tmp in dict:
                    dict[tmp].append(jumsu)
                else:
                    dict[tmp]=[jumsu]

    for k in dict:
        dict[k].sort()

    for que in query:
        qu = que.split(' ')
        qu_jogun = qu[:-1]
        qu_jumsu = int(qu[-1])
        while 'and' in qu_jogun: # and 제거
            qu_jogun.remove('and')
        while '-' in qu_jogun: # -제거
            qu_jogun.remove('-')
        qu_jogun = ''.join(qu_jogun)

        
        if qu_jogun in dict:
            scores = dict[qu_jogun]
            if scores:
                enter = bisect_left(scores,int(qu_jumsu))

                answer.append(len(scores)-enter)
        else:
            answer.append(0)

    return answer

