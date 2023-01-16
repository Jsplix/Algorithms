import sys
input = sys.stdin.readline
# [BOJ] 11401 이항 계수 3 / 페르마의 소정리, 수학, 정수론, 분할 정복
MOD = 1000000007
def fact(N):
    x = 1
    for i in range(2, N+1):
        x = (x*i)%MOD
    return x

def solve(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    
    k = solve(base, exp//2)

    if exp % 2:
        return k*k*base%MOD
    else:
        return k*k%MOD

n, k = map(int, input().split())

deno = fact(n)
numer = fact(n-k) * fact(k) % MOD

print(deno*solve(numer, MOD-2) % MOD)

# 나머지 분배 법칙은 나눗셈에서는 성립이 되지 않기 때문에 분모를 제곱수로 표현해서 곱의 형태로 나타낸다음
# 나머지 분배 법칙을 이용하여 해결(print문의 수식이 나머지 분배법칙을 활용한 것임.)