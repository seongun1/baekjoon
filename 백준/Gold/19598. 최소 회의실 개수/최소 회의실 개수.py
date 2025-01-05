import sys
input = sys.stdin.readline
import heapq
n = int(input())
arr =[]
c =[] #회의실 리스트
for _ in range(n):
    arr.append(list(map(int,input().split())))
# #print(arr)
arr.sort(key= lambda x : x[0])
#print(arr)
# 힙큐 --> 제일 빨리 끝나는 시간 기준으로 정렬해주는 큐
heapq.heappush(c,arr[0][1])
for start,end in arr[1:]:
    if c[0] <= start:
        heapq.heappop(c) #회의실 재사용
    heapq.heappush(c,end)
print(len(c))