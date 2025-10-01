import sys

num = int(sys.stdin.readline().strip())
if num <2:
    print(0)
    sys.exit(0)
#소수 판별 -> 에라토스테네스의 채
def return_prime(num):
    isprime = [True] *(num+1)

    isprime[0] = isprime[1] = False
    p =2
    while(p*p <= num):
        if isprime[p]:
            for x in range(p*p , num+1 ,p):
                isprime[x] = False
        p +=1

    return [i for i,flag in enumerate(isprime) if flag]

primes = return_prime(num)

# 연속된 구간일 경우 --> 투 포인터로 계산
left =0
val =[]
ans =0
#print(primes)
for right in range(len(primes)):
    val.append(primes[right])
    while sum(val) > num and left <= right:
        val.pop(0)
        left +=1
    if sum(val) == num:
        #print(val)
        ans +=1
print(ans)