def check(m, n, board):
    graph =[[0 for _ in range(n)]for _ in range(m)]
    count = 0
    
    for i in range(m-1):
        for j in range(n-1):
            a= board[i][j]
            b=board[i][j+1]
            c=board[i+1][j]
            d = board[i+1][j+1]
            if a== b==c==d and a !='0':
                graph[i][j],graph[i+1][j],graph[i][j+1],graph[i+1][j+1] = 1,1,1,1
                
    for i in range(m):
        for j in range(n):
            if graph[i][j] ==1:
                count +=1
                board[i][j] ='0'
                
    if count ==0:
        return 0
    #터진 부분 채우기
    for i in range(m-2,-1,-1):
        for j in range(n):
            k=i
            while 0<= k+1 < m and board[k+1][j] =='0':
                k+=1
            if k !=i:
                board[k][j] = board[i][j]
                board[i][j] ='0'
                
    return count
def solution(m,n,board):
    answer =0
    board = list(map(list,board))
    
    while True:
        tmp = check(m,n,board)
        if tmp ==0:
            break
        answer += tmp
    return answer