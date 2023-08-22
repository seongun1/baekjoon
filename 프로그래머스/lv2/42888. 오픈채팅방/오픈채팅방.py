def solution(record):
    answer = []
    #채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record
    Enter = "님이 들어왔습니다."
    Leave = "님이 나갔습니다."
    kakao=dict()
    for rec in record:
        rec = rec.split()
        if len(rec) ==3:
            kakao[rec[1]] = rec[2]
    for rec in record:
        rec = rec.split()
        if rec[0] =='Enter':
            answer.append(kakao[rec[1]]+Enter)
        elif rec[0] == 'Leave':
            answer.append(kakao[rec[1]]+Leave)
    return answer