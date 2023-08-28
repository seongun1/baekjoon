import sys
input = sys.stdin.readline

n,k = map(int,input().split())
num = list(map(str,input().rstrip()))
num_stack = []
for i in range(n):
    while k>0 and num_stack and num_stack[-1] < num[i]:
        k -=1
        num_stack.pop()
    num_stack.append(num[i])
num_stack = ''.join(num_stack)
if k>0:
    num_stack = ''.join(num_stack[:len(num_stack) - k])
print(num_stack)