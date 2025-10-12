import sys
from collections import deque

s = sys.stdin.readline().strip()



ans = [' '] * len(s)

middle =[]
def find_middle(array,left,right): #문자열상 가장 사전에 가까운 값을 return. 
    arr = list(array[left:right])
    arr.sort()
    middle_str = arr[0]
    return s.find(middle_str,left,right)
    

count =0
arr = [(0,len(s))]

while arr:
    left,right = arr.pop()
    if left >= right:
        continue
    
    middle = find_middle(s,left,right)
    ans[middle] = s[middle]
    for a in ans:
        if a == ' ':
            continue
        print(a,end='')
    print()

    arr.append((left,middle))
    arr.append((middle+1,right)) 
    #print(left,middle,right,count)