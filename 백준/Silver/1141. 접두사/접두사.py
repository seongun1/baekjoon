import sys
input = sys.stdin.readline
n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key =len)
#print(words)

ans =0
for i in range(n):
    flag = False
    for j in range(i+1,n):
        if words[i] == words[j][0:len(words[i])]:
            flag = True
            break
    if not flag:
        ans +=1
print(ans)
    
