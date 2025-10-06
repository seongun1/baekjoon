from collections import defaultdict

def solution(name, yearning, photo):
    score = defaultdict(int)
    for i, n in enumerate(name):
        score[n] = yearning[i]
    #print(score)
    answer= []
    
    for p in photo:
        tmp =0
        for person in p:
            tmp += score[person]
        answer.append(tmp)
    return answer