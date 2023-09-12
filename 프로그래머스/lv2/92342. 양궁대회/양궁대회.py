from collections import deque

def bfs(n, info):
    answer_arrow =[]
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    max_gap =0 # 현재 저장되어 있는 최대 차이 점수

    while q:
        focus,arrow =q.popleft()

        if sum(arrow) ==n: #주어진 화살을 다 쏜 경우
            apeach,lion = 0,0 # 각각 캐릭터의 점수
            for i in range(11):
                if not (info[i] ==0 and arrow[i] ==0):
                    if info[i] >= arrow[i]: #어피치가 이김.
                        apeach += 10-i
                    else:
                        lion += 10-i
            if apeach < lion: #라이언이 이길 때
                gap = lion - apeach
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    max_gap = gap
                    answer_arrow.clear()
                answer_arrow.append(arrow)

        elif sum(arrow) >n: #화살을 더 쏜 경우 -> 버림.
            continue

        elif focus == 10: # 화살을 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus]  = n - sum(tmp) # 남은 화살 다 쏘기
            q.append((-1,tmp))

        else: #화살 쏘기 (아직 n보다 덜 쐈을때)
            tmp = arrow.copy()
            tmp[focus] = info[focus] +1
            q.append((focus+1,tmp))
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1,tmp2))
    return answer_arrow

def solution(n, info):
    winlist = bfs(n,info)

    if not winlist:
        return [-1]
    elif len(winlist) ==1:
        return winlist[0]
    else:
        return winlist[-1]
    

