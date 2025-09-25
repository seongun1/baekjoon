def solution(players, m, k):
    answer = 0
    server = []
    
    def count_live_server(time):
        live_server = 0
        server.sort()
        for start,end in server:
            if end > time: #현재시각 대비 끝 시간이 지나지 않은 살아있는 서버 계산(종료 : 5시 ,현재시각 : 3시)
                live_server +=1
        
        return live_server
    
    for time,player in enumerate(players):
        live_server = count_live_server(time)
        if player // m > live_server: #만약 이용자의 수보다 서버의 수가 적다면 --> 증설
            live_server = count_live_server(time)
            #print(time,player,live_server,server)
            server_establish = player // m - live_server
            answer += server_establish
            for _ in range(server_establish): #증설된 서버의 갯수만큼 서버 만들기
                server.append([time,time+k])
            
    return answer