import sys
sys.setrecursionlimit(1000000) 
N,K=map(int,sys.stdin.readline().split()) 


def check(n,k):
  val=1
  while val<n: 
    val*=2
  if k==1: 
    return val-n
  else: 
    val//=2 
    return check(n-val,k-1) 


if N<K:
  print(0) 
else:
  print(check(N,K))