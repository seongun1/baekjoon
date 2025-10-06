def solution(data, ext, val_ext, sort_by):
    order ={'code' :0 , 'date':1,'maximum':2,'remain':3 }
    answer = []
    for d in data:
        if ext =='code' and d[order[ext]] < val_ext : #ext 겂아 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
            answer.append(d)
        elif ext == 'date' and d[order[ext]] < val_ext:
            answer.append(d)
        elif ext == 'maximum' and d[order[ext]] < val_ext:
            answer.append(d)
        elif ext == 'remain' and d[order[ext]] < val_ext:
            answer.append(d)
    
    #정렬하기
    answer.sort(key = lambda x: x[order[sort_by]])
            
    return answer