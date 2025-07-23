from itertools import combinations

def solution(n, q, ans):
    candidates = list(combinations(range(1,n+1),5))
    for arr , count in zip(q,ans):
        candidates = [c for c in candidates if len(set(arr) & set(c)) == count]
        # for c in candidates[:]: #삭제 시 복사본을 순회하지 않으면 remove 하고 문제가 생김
        #     if len(set(arr) & set(c))  != count:
        #         candidates.remove(c)
    return len(candidates)