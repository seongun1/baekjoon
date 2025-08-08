def solution(targets):
    answer = 0
    targets = sorted(targets ,key = lambda x : x[1])
    missile = 0
    for x,y in targets:
        if x<missile<y:
            continue
        else:
            missile = y - 0.1
            answer +=1
    return answer