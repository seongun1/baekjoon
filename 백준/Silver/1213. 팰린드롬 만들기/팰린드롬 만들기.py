import sys
input = sys.stdin.readline

name = input().strip()
name = list(name)
name.sort()
#print(name)

def pelindrome_name(name):
    dict = {}
    for n in name:
        if n in dict:
            dict[n] +=1
        else:
            dict[n] =1
    #print(dict)
    odd = False
    for a in dict.values():
        if a%2 and not odd:
            odd = True
        elif a%2 and odd:
            return "I'm Sorry Hansoo"
    left =[]
    middle = ''
    right =[]
    for char in dict.keys():
        count = dict[char]
        left.append(int(count/2)  * char)
        right.append(int(count/2) * char)
        if count %2:
            middle += char
    answer = ''.join(left) + middle + ''.join(right[::-1])
    return answer
print(pelindrome_name(name))