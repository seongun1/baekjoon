import sys
input =sys.stdin.readline
n,k = map(int,input().split())
arr =[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
#print(arr)

count =0
while(k):
    for a in arr:
        if a>k:
            continue
        coin = k // a
        k -= a * coin
        count +=coin
        break
print(count)
