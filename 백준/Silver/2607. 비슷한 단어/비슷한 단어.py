import sys
from collections import defaultdict
n =int(sys.stdin.readline())

s = sys.stdin.readline().strip()
arr = [list(input().strip()) for _ in range(n-1)]

dic =defaultdict(int)

s = list(s)
s.sort()
for a in arr:
    a.sort()

#print(s,arr)

for i in s:
    dic[i] +=1

dic_k = dic.keys()
dic_v = dic.values()
def sum_abs_diff(d1,d2):
    keys = set(d1.keys()) | set(d2.keys())
    total = 0
    for k in keys:
        total += abs(d1.get(k,0) - d2.get(k,0))
    return total

def is_same(candi):
    total = sum_abs_diff(dic,candi)
    if total == 0:
        return True
    elif sum(candi.values()) == sum(dic.values()) and total == 2:
        return True
    elif abs(sum(candi.values()) - sum(dic.values())) ==1 and total ==1:
        return True
    return False

ans =0
for a in arr:
    candi = defaultdict(int)
    for i in a:
        candi[i] +=1
    #print(candi)
    if is_same(candi):
        ans +=1
    
print(ans)