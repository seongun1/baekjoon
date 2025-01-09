import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))
group = []
for i in range(len(arr)-1):
    tmp = arr[i+1] - arr[i]
    group.append((arr[i+1],arr[i],tmp))
group.sort(key= lambda x : x[2],reverse=True)
#print(group)
diff = 0
for i in range(k-1):
    diff += group[i][2]
print((arr[len(arr)-1] - arr[0]) - diff)