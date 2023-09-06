import sys
input = sys.stdin.readline

n = int(input())

#단, 서로소인 서로 다른 두 자연수는 다른 색으로 칠해야 한다. 
#최소한의 색을 써서 모든 자연수를 칠하는 방법을 찾는 프로그램을 작성하자.
answer = [0 for i in range(n+1)]
answer[1] =1
if n>=2:
    answer[2] =2
color =3

for i in range(3,n+1):
    if i % 2 == 0: #만약 2의 배수일 경우
        answer[i] = answer[2]
    elif answer[i] ==0:
        answer[i] = color
        start =2 #그 수의 배수까지 다 같은 색으로 칠한다.
        while (i * start <=n):
            answer[i*start] = color
            start +=1
        color +=1

print(max(answer))
for i in range(1,n+1):
    print(answer[i],end =' ')