import sys
input = sys.stdin.readline

a,b = map(int,input().split())
def count(a,b):
    count=1
    while(a!=b):
        if b ==0:
            return -1
        count +=1
        if not b%2:
            b //=2
        elif b%10 ==1:
            b //=10
            #print(b)
        else:
            return -1
    return count

print(count(a,b))