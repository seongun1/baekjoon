import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
#print(*arr)

def print_answer():
    if n==1:
        return 0
    cnt =0
    max_end =0
    current_step =0
    for i in range(n):
        current_step = max(current_step,i + arr[i])

        if i == max_end:
            cnt +=1
            max_end = current_step

            if max_end >= n-1: 
                return cnt
            if max_end == i:
                return -1
    
    return -1
print(print_answer())