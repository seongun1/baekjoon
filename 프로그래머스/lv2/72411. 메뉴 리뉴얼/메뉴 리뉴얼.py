from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    #각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders
    # "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course
    menu =dict()#메뉴 후보
    for i in course:
        tmp =[]
        for j in orders:
            menu = combinations(sorted(j),i)
            tmp += menu
        counter =Counter(tmp)
        if len(counter) !=0 and max(counter.values()) != 1:
            answer += [''.join(k) for k in counter if counter[k] == max(counter.values())]
    return sorted(answer)
