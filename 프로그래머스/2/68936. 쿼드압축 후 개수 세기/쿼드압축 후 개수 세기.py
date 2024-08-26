def solution(arr):
    global answer
    answer = [0,0]
    quad(arr,answer,len(arr))
    return answer
def quad(arr,start,n):
    a,b,target = start[0],start[1],arr[start[0]][start[1]]
    for i in range(n):
        for j in range(n):
            if arr[a+i][b+j] != target:
                quad(arr,[a,b+n//2],n//2)
                quad(arr,[a+n//2,b], n//2)
                quad(arr,[a,b],n//2)
                quad(arr,[a+n//2,b+n//2],n//2)
                return
    answer[target]+=1