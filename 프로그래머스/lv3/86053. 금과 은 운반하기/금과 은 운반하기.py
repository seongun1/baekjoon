def solution(a, b, g, s, w, t): 
    #이진탐색
    #a:필요한 금의 양 b:필요한 은의 양 g:금을 가지고 있는 갯수 s: 은을 가지고 있는 갯수 w:실을 수 있는 무게 t:운반하는데 걸리는 시간
    #https://yabmoons.tistory.com/714 참고
    answer = 4*10**14 + 10**5 #광물을 옮길 수 있는 최댓값
    start =0
    end = 4*10**14 + 10 ** 5
    while end >= start:
        mid = (end+start)//2
        gold =0
        silver =0
        add =0 #주어진 시간 내 옮길 수 있는 광물 (금 + 은)의 양
        for i in range(len(t)):
            g_move = g[i]
            s_move = s[i]
            w_move = w[i]
            time_spend = t[i]
            move_cnt = mid // (time_spend *2)
            if mid %(time_spend*2) >= time_spend:
                move_cnt +=1
            gold += min(g_move,move_cnt * w_move)
            silver += min(s_move,move_cnt*w_move)
            add += min(g_move + s_move,move_cnt*w_move)
        if gold >= a and silver >= b and add >= a+b:
            end = mid -1
            answer = min(mid,answer)
        else:
            start = mid + 1 
    return answer