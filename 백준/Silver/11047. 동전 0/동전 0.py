import sys
input =sys.stdin.readline
n,k = map(int,input().split())
arr =[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
#print(arr)

count =0
for i in arr:
    count += k //i
    k = k%i
print(count)
