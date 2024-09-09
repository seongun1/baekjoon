n = int(input())
line =1
while n > line:
    n -=line
    line +=1
if line%2: #홀수
    num1 = line - n +1 #분모
    num2 = n #분자
else:
    num1 = n
    num2 = line - n +1
print(num1,"/",num2,sep ='')
