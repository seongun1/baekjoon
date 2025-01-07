import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
arr.sort(key= lambda x : len(x),reverse= True)
#print(arr)
alpha ={}
for word in arr:
    length = len(word)
    for i,char in enumerate(word):
        power = 10 **(length -1 -i)
        if char in alpha:
            alpha[char] += power
        else:
            alpha[char] = power
alpha = dict(sorted(alpha.items() , key= lambda x : x[1],reverse = True))
#print(alpha)
val = 9
for a in alpha.keys():
    alpha[a] = val
    val -=1
#print(alpha)
ans =0
for word in arr:
    length = len(word)
    tmp =0
    for i, char in enumerate(word):
        tmp += alpha[char] * (10**(length - i -1))
    #print(tmp)
    ans += tmp
print(ans)