from collections import deque
def solution(storage, requests):
    answer = 0
    arr = deque()
    tmp = ['2'] * (len(storage[0]) +2)
    arr.appendleft(tmp.copy())
    #print(arr)
    for s in storage:
        s = deque(s)
        s.append('2')
        s.appendleft('2')
        arr.append(list(s))
    arr.append(tmp.copy())

    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n,m = len(arr) , len(arr[0])
    def remove_container(box, outside):
        if outside:
            while box:
                x,y = box.pop()
                arr[x][y] = '0'
        else:
            while box:
                x,y = box.pop()
                arr[x][y] = '1'
                
    def check_outside(n,m):
        flag = False
        while(1):
            flag = False
            for x in range(n):
                for y in range(m):
                    if arr[x][y] =='1': #바깥과 연결되어 있는지 확인
                        for i in range(4):
                            nx,ny = x+dx[i] , y+dy[i]
                            if 0<=nx<n and 0<=ny<m and (arr[nx][ny] =='2' or arr[nx][ny] == '0'):
                                arr[x][y] = '0'
                                flag = True
                                break
            if not flag:
                break
    #print(arr)
    for r in requests:
        if len(r) ==1: #지게차 출고
            remove_box = []
            for x in range(n):
                for y in range(m):
                    if arr[x][y] == r: #만약 같은 게 있다면 주변 확인
                        for i in range(4):
                            nx ,ny = x +dx[i] , y + dy[i]
                            if 0<=nx<n and 0<=ny<m and (arr[nx][ny] == '0' or arr[nx][ny] =='2'):
                                remove_box.append((x,y))
                                break
            remove_container(remove_box, True)
        elif len(r) == 2: #크레인 출고
            char = r[0]
            outside_box =[]
            inside_box =[]
            for x in range(n):
                for y in range(m):
                    if arr[x][y] == char:
                        outside = False
                        #print(x,y,arr[x][y])
                        for i in range(4): #외곽판정
                            nx,ny = x+dx[i] , y+dy[i]
                            #print(nx,ny, x,y,arr[nx][ny])
                            if 0<=nx<n and 0<=ny<m and (arr[nx][ny] == '0' or arr[nx][ny] == '2'):
                                #print('--' ,x,y,arr[x][y])
                                outside_box.append((x,y))
                                outside = True
                                break
                        if not outside:
                            inside_box.append((x,y)) #빠진건 맞지만, 외곽과 닿아있는것은 아닌 박스
            remove_container(outside_box,True)
            remove_container(inside_box,False)
        
        check_outside(n,m)
        
             
    check_outside(n,m)
    for a in arr:
        #print(a)
        for i in a:
            if i.isalpha():
                answer +=1
    return answer