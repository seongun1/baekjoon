import sys
input = sys.stdin.readline

t = int(input())

def fibonacchi_make_upto(n):
    f =[0,1]
    while (f[-1] <= n):
        f.append(f[-1] + f[-2])
    return f[:-1]
#print(f)
for _ in range(t):
    val = int(input())
    arr= []
    f = fibonacchi_make_upto(val)
    while (val >0):
        for i in range(len(f)-1,-1,-1):
            if f[i] <= val:
                arr.append(f[i])
                val -= f[i]
                break
    arr.sort()
    print(*arr)