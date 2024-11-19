import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    max_price = 0
    interest =0
    for price in reversed(arr):
        if max_price < price:
            max_price = price
        else:
            interest += max_price - price
    print(interest)