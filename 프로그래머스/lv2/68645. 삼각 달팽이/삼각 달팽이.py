def solution(n):
    answer = []
    # 처음에는 0으로 초기화 한 이중 배열의 크기를 미리 만든다.
    index = [[]for j in range (1,n+1)]
    tmp =1
    for i in range (n):
        index[i] = [0] * tmp
        tmp +=1
    nx =0
    ny = -1
    number = 1
    # index 배열에 값을 채워 넣음.
    for i in range (n):
        for j in range (i,n): # x,y를 기준으로, 세로가 y 가로방향이 x 내려가는게 + / 오른쪽이 +  
            if i% 3 == 0: # 위 -> 아래
                ny += 1
            elif i % 3 ==1: # 왼쪽 -> 오른쪽으로 회전
                nx += 1
            else: # 아래 -> 위로 가는데 각각 배열의 값이 하나씩 줄어야 함.
                ny -=1
                nx -=1
            index[ny][nx] =number
            number +=1

    for i in index:
        answer += i

    return answer