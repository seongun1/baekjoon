def factorial(n):
    num =1
    for i in range(1,n+1):
        num *= i
    return num

t = int(input()) #테스트 게이스의 갯수
bridge = []
for _ in range(t):
    bridge.append(list(map(int,input().split())))
#print(bridge)
answer = []
for a,b in bridge:
    print(int(factorial(b) / (factorial(a) * factorial(b-a))))
