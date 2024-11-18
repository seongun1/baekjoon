import sys
input = sys.stdin.readline

t= int(input())
# 프린트 코드 간결화
def print_answer(tmp):
    return max(abs(tmp[i] - tmp[i+1]) for i in range(len(tmp) -1))
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    start,end = 0,n-1
    answer =[0]*n
    for i in range(n):
        if not i%2:
            answer[start] = arr[i]
            start +=1
        else:
            answer[end] = arr[i]
            end -=1
    print(print_answer(answer))