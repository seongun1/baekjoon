import sys
input = sys.stdin.readline
import re 
N = int(input()) #테스트 케이스

sign = [' ','+','-'] # 덧샘 뺄셈 숫자 붙이기 
def process (expr):
        #print(expr,'before')
        expr = re.findall(r'\d+|[+\- ]',expr)
        op = '/' #초깃값
        arr =[]
        #print(expr)
        #공백을 파싱 단계에서 미리 합쳐야 함.근데 for문으로 하면 arr의 길이가 달라지기 때문에 while문으로 하는 게 좋음.
        i = 0
        while i < len(expr):
            if expr[i].isdigit():
                num = expr[i]
                while i+2 < len(expr) and expr[i+1] == ' ' and expr[i+2].isdigit():
                    num += expr[i+2]
                    i +=2
                arr.append(num)
                i +=1
            else:
                arr.append(expr[i])
                i +=1
        #print('arr=',arr)
        op ='/'
        score =0
        #계산하기
        for e in arr:
            if e.isdigit():
                if op =='/': #초깃값
                    score = int(e)
                elif op =='+':
                    score += int(e)
                elif op == '-':
                    score -= int(e)
            else:
                op = e
        if score == 0:
            return True
        return False

def dfs(idx,expr):
        global answer
        if idx >num:
            if process(expr):
                answer.append(expr)
            return
        for op in sign:
            dfs(idx+1,expr + op + str(idx))
def print_answer(arr):
    for a in arr:
        print(''.join(a))

for _ in range(N):
    answer =[]
    num = int(input())
    dfs(2,"1")
    print_answer(answer)
    print()
    