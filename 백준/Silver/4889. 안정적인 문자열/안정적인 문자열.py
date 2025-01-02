import sys
input = sys.stdin.readline
ans =[]
def print_answer():
    num =1
    while(1):
        tmp = input().strip()
        tmp = list(tmp)
        if tmp[0] == '-':
            break
        #print(tmp)
        arr =[]
        for t in tmp:
            if t =='{':
                arr.append(t)
            else:
                if len(arr) !=0 and arr[-1]!= t:
                    arr.pop()
                # elif len(arr) !=0 and arr.pop() == t:
                #     arr.append(t)
                else:
                    arr.append(t)
        cnt =0
        while (arr):
            #print(arr)
            a = arr.pop()
            b = arr.pop()
            if a != b:
                cnt +=2
            else:
                cnt +=1
        print(f"{num}. {cnt}")
        num +=1
        
print_answer()
