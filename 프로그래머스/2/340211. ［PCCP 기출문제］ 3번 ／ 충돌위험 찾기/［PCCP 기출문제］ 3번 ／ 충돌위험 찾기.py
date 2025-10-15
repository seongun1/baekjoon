from collections import defaultdict

def solution(points, routes):
    """
    points: list of [r,c] for points 1..n
    routes: list of lists: each route is [p1, p2, ..., pm] (1-based indices)
    반환: 문제의 정의대로 '동일 시간·동일 좌표에 2대 이상 모인 (time,coord) 횟수의 합'
    """
    arr = defaultdict(int)  # key = (time, r, c) -> count

    for route in routes:
        start = list(points[route[0]-1])  # 복사
        time = 0
        arr[(time, start[0], start[1])] += 1

        # 각 구간(인접 포인트 쌍)마다 이동 시뮬레이션
        for j in range(1, len(route)):
            end = list(points[route[j]-1])
            while start[0] != end[0] or start[1] != end[1]:
                time += 1
                # r 좌표 변화 우선
                if start[0] != end[0]:
                    if start[0] > end[0]:
                        start[0] -= 1
                    else:
                        start[0] += 1
                else:
                    # r이 같을 때만 c를 바꾼다
                    if start[1] > end[1]:
                        start[1] -= 1
                    else:
                        start[1] += 1
                arr[(time, start[0], start[1])] += 1
        # 마지막 점 도착 후 로봇은 떠남 -> 이 시점 이후 기록하지 않음

    # (time, coord) 당 2대 이상이면 1씩 더함
    answer = sum(1 for cnt in arr.values() if cnt >= 2)
    return answer
