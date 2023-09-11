def solution(name):
    answer = 0
    min_move = len(name) -1
    pointer =0
    while name[min_move] =='A' and min_move >0:
        min_move -=1
    if min_move <0:
        return answer
    
    for i,alpha in enumerate(name):
        answer += min(ord(alpha) - ord('A') , ord('Z') - ord(alpha) +1)
        pointer = i+1
        while pointer< len(name) and name[pointer] =='A':
            pointer +=1
        min_move = min(min_move, i + i + len(name) - pointer, i + 2 * (len(name) -pointer))
    answer += min_move
    return answer

