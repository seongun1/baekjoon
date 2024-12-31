import sys
input = sys.stdin.readline
from itertools import combinations
n = int(input())

arr =[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

def make_tri():
    #print(combi)
    for i in range(n-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            return arr[i] + arr[i+1] + arr[i+2]
    return -1
print(make_tri())