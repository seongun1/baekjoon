import sys
sys = sys.stdin.readline

t= int(input())
def print_answer(tmp):
    ans =0
    for i in range(n-1):
        if ans < abs(tmp[i] - tmp[i+1]):
            ans = abs(tmp[i] - tmp[i+1])
    return ans
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    index,start,end = 0,0,n-1
    answer =[0]*n
    start_flag = True
    for i in range(n):
        if start_flag:
            answer[start] = arr[i]
            start +=1
            start_flag = not start_flag
        else:
            answer[end] = arr[i]
            end -=1
            start_flag = not start_flag
    print(print_answer(answer))
    