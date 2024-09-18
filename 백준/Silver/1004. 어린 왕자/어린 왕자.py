import sys
input = sys.stdin.readline
t= int(input())

def print_answer():
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input()) # 행성계의 갯수
    arr = []
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    answer =0
    #print(arr)
    for a in arr:
        if ((x1 - a[0])**2) + ((y1 - a[1]) **2) < a[2] **2:
            if ((x2 - a[0]) **2) + ((y2 - a[1])**2) < a[2] **2:
                continue
            else:
                answer +=1
        elif (x2 - a[0])**2 + (y2 - a[1]) **2 < a[2] **2:
            answer +=1
    return answer
for _ in range(t):
    print(print_answer())