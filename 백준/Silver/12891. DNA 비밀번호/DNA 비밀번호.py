import sys
input = sys.stdin.readline
from collections import deque
s,p = map(int,input().split())
arr = str(input().rstrip())
arr = list(arr)
a,c,g,t = map(int,input().split())
#print(arr)

first,end,cnt =0,p,0

dna_str=arr[first:end]
dna ={'A':0,'C':0,'G':0,'T':0}
for char in dna_str:
        dna[char] +=1
#print(dna)

while(1):
    if dna['A'] >=a and dna['C'] >=c and dna['G']>=g and dna['T']>=t:
        #print(dna_str)
        cnt +=1
    if end >= s:
        break
    if arr[first] =='A':
        dna['A'] -=1
    elif arr[first] =='C':
        dna['C'] -=1
    elif arr[first] =='G':
        dna['G'] -=1
    else:
        dna['T'] -=1
    first +=1
    end +=1
    dna[arr[end-1]] +=1
    #print(dna,'++')
print(cnt)