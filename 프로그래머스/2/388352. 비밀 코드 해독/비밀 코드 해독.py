from itertools import combinations

def solution(n, q, ans):
    arr = [i for i in range(1,n+1)]
    candi = list((combinations(arr,5)))
    answer =[]
    def filter_code (ans,q,candi):
        for secret_code in candi:
            flag = True
            for i,code in enumerate(q):
                if len((set(secret_code) & set(code))) != ans[i]:
                    flag = False
                    break
            if flag:
                answer.append(secret_code)
                
    filter_code(ans,q,candi)
    
    return len(answer)