def solution(schedules, timelogs, startday):
    answer = 0
    for i,time in enumerate(timelogs):
        s_margino = schedules[i] + 10
        if (s_margino %100) >=60:
            s_margino += 40
        gift = True
        s_startday = startday
        print(time)
        for t in time:
            #print(s_margino , t , s_startday,t>s_margino)
            if s_startday == 6 or s_startday == 7:
                s_startday = (s_startday%7) +1
                continue
            if t > s_margino:
                #print("TRUE--")
                gift = False
                break
            #print((s_startday %7) +1)
            s_startday = (s_startday%7) +1
        if gift:
            answer +=1
                
    return answer