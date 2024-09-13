from itertools import combinations

arr =[]
while(1):
    tmp = list(map(int,input().split()))
    if tmp[0] == 0:
        break
    arr.append(tmp)
#print(arr)

def nCr(arr):
    answer = []
    arr.pop(0)
    answer = list(combinations(arr,6))
    return answer
for a in arr:
    answer = nCr(a)
    for a in answer:
        for k in a:
            print(k,end=' ')
        print()
    print()