import sys
input = sys.stdin.readline
# [BOJ] 1124 언더프라임 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
MX = int(1e6)
a, b = map(int, input().split())

Eratosthenes_Sieve = [0, 0] + [1 for _ in range(MX)]
for i in range(2, int(MX**0.5)+1):
    if Eratosthenes_Sieve[i] == 0: continue
    for j in range(i+i, MX+1, i):
        Eratosthenes_Sieve[j] = 0
prime_num = [ i for i in range(2, MX+1) if Eratosthenes_Sieve[i] ]

def solve(a):
    check = []
    idx = 0
    while True:
        if a % prime_num[idx] == 0:
            check += [prime_num[idx]]
            a //= prime_num[idx]
        else: idx += 1

        if a == 1: return len(check) if len(check) in prime_num else -1

# 2~10 / 4, 6, 8, 9, 10
answer = 0
for i in range(a, b+1):
    if solve(i) != -1: answer += 1
print(answer)