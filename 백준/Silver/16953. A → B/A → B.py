import sys

input = sys.stdin.readline

a,b = map(int,input().split())
def count(a,b):
    count=1
    while(a!=b):
        if b==1:
            return -1
        count +=1
        last_digit = b%10
        if last_digit ==1:
            b = str(b)
            b = list(b)
            b = b[:len(b)-1]
            b = ''.join(b)
            b = int(b)
            #print(b)
        elif not last_digit%2:
            b//=2
        else: # 1이 아닌 홀수인 경우
            return -1
    return count

print(count(a,b))