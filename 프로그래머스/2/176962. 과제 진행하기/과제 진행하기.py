
def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    stop = [] #미룬 과목들
    for i in range(len(plans)-1):
        sub,time,dur = plans[i]
        dur = int(dur)
        hour,minute = int(time[:2]) , int(time[3:])
        n_hour,n_minute = int(plans[i+1][1][:2]) , int(plans[i+1][1][3:])
        between_time = (n_hour - hour) * 60 + (n_minute-minute) #사이 시간 계산
        
        #print(sub,time,between_time , dur)
        if between_time< dur: #그 다음 해야하는 시간보다 만약 남은 숙제 시간이 더 많다면 -> 미뤄야함
            stop.append((sub,dur - between_time))
        elif between_time > dur:
            answer.append(sub)
            between_time -= dur
            #만약 숙제를 다 했는데 시간이 남는다면 -> 남는 시간에 밀린 숙제 해야 함
            if stop:
                for i in range(len(stop)-1 , -1 ,-1):
                    remain_sub , remain_time = stop.pop()
                    if between_time < remain_time:
                    #사이 시간보다 남는 시간이 더 많다면 -> 그 시간만큼 더 하고 다시 stop에 넣어놓기
                        remain_time -= between_time
                        stop.append ((remain_sub,remain_time))
                        break
                    answer.append(remain_sub)
                    between_time -= remain_time 
                    if between_time <=0:
                        break
        elif between_time == dur:
            answer.append(sub)
        #print(sub,time,dur,stop)
        
    answer.append(plans[-1][0]) #마지막 과목은 무조건 끝냄
    
    for s in stop[::-1]:
        answer.append(s[0])
    
    return answer