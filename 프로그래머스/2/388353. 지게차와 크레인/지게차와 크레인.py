def solution(storage, requests):
    arr = []
    arr.append(list('0' * (len(list(storage[0])) +2)))
    for s in storage:
        arr.append(list('0'+ s+ '0'))
    arr.append(list('0' * (len(list(storage[0])) +2)))
    
    #print(arr)
    n,m = len(arr), len(arr[0])
    answer = 0 #남은 컨테이너의 수
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    def check_outside(x,y): #지게차의 경우, 바깥과 연결되어 있는지 확인
        for i in range(4):
            nx,ny = x + dx[i], y +dy[i]
            if 0<= nx < n and 0<= ny < m and arr[nx][ny] == '0':
                #print('--',nx,ny,x,y)
                #arr 범위 안에 있고 바깥과 연결되어 있다면 -> 지게차 제거 가능
                return True
        return False
    
    def update_outside(): #크레인으로 꺼내진 블록 중에서(-1), 바깥과 연결되어 있는지 확인
        while(1):
            flag = False
            for x in range(n):
                for y in range(m):
                    if arr[x][y] == '-1': #크레인으로 꺼내진 것이 있다면
                        for i in range(4): #상하좌우 중 바깥과 연결된 블록이 있는지 계산
                            nx,ny = x + dx[i], y + dy[i]
                            if 0<= nx < n and 0<= ny < m and arr[nx][ny] == '0': 
                                arr[x][y] = '0'
                                flag = True
                                break
            if not flag: #더 이상 업데이트 할 것이 없다면
                break
                            
    #requests 별로 계산
    for req in requests:
        req = list(req)
        #print(len(req))
        val = req[0] #비교해야 할 알파벳
        if len(req) == 2: #크레인의 경우 -> 상관하지 않고 다 꺼냄
            for x in range(1,len(arr)-1):
                for y in range(1,len(arr[0]) -1):
                    if arr[x][y] == val:
                        arr[x][y] ='-1' #마킹만 하기
        else: #지게차의 경우
            for x in range(1,len(arr)-1):
                for y in range(1,len(arr[0])-1):
                    if arr[x][y] == val and check_outside(x,y): #알파벳과 같고 바깥과 연결되어 있다면 부숨
                        arr[x][y] = '-1' #지게차가 부숴도 하나의 루프 당시에는 -1로 표시
                        
        update_outside()
        #print(arr)
        
    for x in range(n):
        for y in range(m):
            if arr[x][y] != '-1' and arr[x][y] != '0':
                answer +=1
    return answer