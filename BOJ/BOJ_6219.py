import sys
input = sys.stdin.readline
# [BOJ] 6219 소수의 자격 / 수학, 정수론, 소수 판정, 에라토스테네스의 체
a, b, d = map(int, input().split())
Eratosthenes_Sieve = [1 for _ in range(b+1)]

for i in range(2, int(b+1**0.5)):
    if not Eratosthenes_Sieve[i]: continue
    for j in range(i+i, b+1, i):
        Eratosthenes_Sieve[j] = 0

cnt = 0
prime_num = [i for i in range(a, b+1) if Eratosthenes_Sieve[i]]
for p in prime_num:
    if str(d) in str(p): cnt += 1

print(cnt)