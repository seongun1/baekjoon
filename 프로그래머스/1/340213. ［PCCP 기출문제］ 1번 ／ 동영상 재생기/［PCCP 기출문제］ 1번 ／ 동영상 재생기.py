def solution(video_len, pos, op_start, op_end, commands):
    if int(op_start[0:2] + op_start[3:]) <= int(pos[0:2] + pos[3:]) <= int(op_end[0:2] + op_end[3:]):
        pos = op_end
        
    answer = pos
    minute = int(answer[:2])
    seconds = int(answer[3:])
    for c in commands:
        if c == "next":
            if 60 * minute + seconds  + 10> 60 * int(video_len[0:2])  + int(video_len[3:]):
                if seconds +10 >=60:
                    minute +=1
                seconds = int(video_len[3:])
            else: seconds +=10
            #print(seconds)
        elif c == "prev":
            if seconds >=10:
                seconds -=10
            elif seconds <10 and minute >= 1:
                seconds += 50 #60초를 주고 10초를 가져갔으므로
                minute -=1
            elif seconds < 10 and minute < 1:
                seconds =0
        if int(op_start[0:2]) * 60 + int(op_start[3:]) <= 60 * minute + seconds <= int(op_end[0:2]) * 60 + int(op_end[3:]):
            minute,seconds = int(op_end[0:2]) , int(op_end[3:])
                
    if seconds >=60:
        minute += seconds // 60
        seconds = seconds % 60
        
    if minute < 10:
        minute = str(0) + str(minute)
    if seconds < 10:
        seconds = str(0) + str(seconds)
        
    answer = str(minute) + ':' + str(seconds)
    if int(op_start[0:2] + op_start[3:]) <= int(answer[0:2] + answer[3:]) <= int(op_end[0:2] + op_end[3:]):
        answer = op_end
    
    if int(answer[0:2] + answer[3:]) > int(video_len[0:2] + video_len[3:]):
        answer = video_len
        
    return answer