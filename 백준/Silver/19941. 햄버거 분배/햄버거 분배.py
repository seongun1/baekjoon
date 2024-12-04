import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr =input()
arr = list(arr)
#print(*arr)
cnt =0

visited = [False] *n
#print(visited)
for i in range(n):
    if arr[i] == 'P':
        for j in range(i-k,i+k+1):
            if 0<=j<n and not visited[j] and arr[j] == 'H':
                cnt +=1
                visited[j] = True
                break
print(cnt)