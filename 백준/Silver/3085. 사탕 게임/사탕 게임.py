import sys
input = sys.stdin.readline

n = int(input())
arr =[list(input().rstrip()) for _ in range(n)]

#print(arr)
max_ans=1

def print_answer():
    global max_ans
    def scan():
        global max_ans
        for i in range(n):
            cnt=1
            for j in range(n-1):
                if arr[i][j] == arr[i][j+1]:
                    cnt +=1
                else: cnt =1
                max_ans = max(cnt,max_ans)
                
            cnt=1
            for j in range(n-1):
                if arr[j][i] == arr[j+1][i]:
                    cnt +=1
                else: cnt=1
                max_ans = max(cnt,max_ans)
    scan()

    for i in range(n):
        for j in range(n-1):
            if j+1<n and arr[i][j] != arr[i][j+1]:
                arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
                scan()
                arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
            if j+1 <n and arr[j][i] != arr[j+1][i]:
                arr[j][i],arr[j+1][i] = arr[j+1][i], arr[j][i]
                scan()
                arr[j][i],arr[j+1][i] = arr[j+1][i], arr[j][i]
print_answer()
print(max_ans)
