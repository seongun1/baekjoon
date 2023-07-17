from itertools import permutations

            
def calculate (n1,n2,operand): #수식에 따라서 다른 return 값을 냄.
    if operand == '+':
        return str(int(n1) + int(n2))
    if operand == '-':
        return str(int(n1) - int(n2))
    if operand == '*':
        return str(int(n1) * int(n2))
            
def calculate_all_num (express,oper):
    array =[]
    temp = ""
    for i in express:
        if i.isdigit():
            temp += i
        else:
            array.append(temp)
            array.append(i)
            temp = ""
    array.append(temp)
    for j in oper:
        stack = []
        while len(array) !=0:
            temp = array.pop(0)
            if temp == j :
                stack.append(calculate(stack.pop(),array.pop(0),j))
            else:
                stack.append(temp)
        array = stack
        
    return abs(int(array[0]))

def solution(expression):
    
    op =['+','-','*']
    op = list(permutations(op,3))
    result = []
    for i in op:
        result.append(calculate_all_num(expression,i))
    
    return max(result)

            
            
    