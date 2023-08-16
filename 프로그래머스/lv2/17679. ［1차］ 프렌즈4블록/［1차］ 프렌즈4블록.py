def check(m, n, board):
    graph =[[0 for _ in range(n)]for _ in range(m)] #높이 m 폭 n
    count = 0
    while True:
        fflag =True
        for i in range(m-1):
            for j in range(n-1):
                a= board[i][j]
                b= board[i][j+1]
                c= board[i+1][j]
                d= board[i+1][j+1]
                if a== b==c==d and a !='0':
                    graph[i][j],graph[i+1][j],graph[i][j+1],graph[i+1][j+1] = 1,1,1,1
                    fflag = False
              
        for i in range(m):
            for j in range(n):
                if graph[i][j] ==1:
                    graph[i][j] =0
                    count +=1
                    board[i][j] ='0'
        if fflag:
            break 

    #터진 부분 채우기
        while True:
            flag = True
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] =='0' and board[i][j] != '0':
                        board[i+1][j] = board[i][j]
                        board[i][j] ='0'
                        flag = False
            if flag:
                break

    return count

    
def solution(m,n,board):
    board = list(map(list,board))
    
    tmp = check(m,n,board)
    return tmp