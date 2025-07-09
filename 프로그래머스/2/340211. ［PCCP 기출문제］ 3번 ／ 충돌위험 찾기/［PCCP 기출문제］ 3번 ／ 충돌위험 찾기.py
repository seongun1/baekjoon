from collections import defaultdict

def solution(points, routes):
    # (t, x, y)별로 로봇이 몇 대 왔는지 기록
    record = defaultdict(int)
    
    for route in routes:
        t = 0
        # 1) t=0, 출발 위치 기록
        cur = points[route[0] - 1].copy()
        record[(t, cur[0], cur[1])] += 1
        
        # 2) 경로의 모든 구간을 순서대로 처리
        for i in range(len(route) - 1):
            start = points[route[i]   - 1]
            end   = points[route[i+1] - 1]
            cur = start.copy()
            
            # 목표 지점에 도달할 때까지 한 칸씩 이동하며 기록
            while (cur[0] != end[0]) or (cur[1] != end[1]):
                t += 1
                # r 좌표부터 맞추고
                if cur[0] < end[0]:
                    cur[0] += 1
                elif cur[0] > end[0]:
                    cur[0] -= 1
                # r 좌표가 같아지면 c 좌표 이동
                elif cur[1] < end[1]:
                    cur[1] += 1
                else:
                    cur[1] -= 1
                
                record[(t, cur[0], cur[1])] += 1

    # 3) 같은 시간·같은 좌표에 2대 이상 모인 이벤트 수 세기
    #    (record[(t,x,y)] >= 2 인 key의 개수가 정답)
    answer = sum(1 for cnt in record.values() if cnt >= 2)
    return answer
