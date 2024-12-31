import sys
input = sys.stdin.readline

n = int(input())
arr= list(map(int,input().split()))
arr.sort()
antena = arr[(n-1)//2]
print(antena)