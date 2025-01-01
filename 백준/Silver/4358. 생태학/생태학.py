import sys
input = sys.stdin.readline

tree = {}
total =0
while(1):
    tmp = input().rstrip()
    if not tmp:
        break
    if tmp not in tree:
        tree[tmp]  = 1
    else:
        tree[tmp] +=1
    total +=1
data = list(tree.keys())
data.sort()

for d in data:
    print(f"{d} {(tree[d] / total) * 100 :.4f}")