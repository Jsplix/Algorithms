from math import isqrt, sqrt
import sys
input = sys.stdin.readline

# [BOJ] 4134 다음 소수 / 브루트 포스, 정수론, 수학, 소수 판정
# **0.5 보다는 sqrt()가 더 정확함. 그러나, 속도측면에서 isqrt가 sqrt보다 빠름
# 심지어 isqrt는 정수로 반환해줌.

MAX = int(4e9)
r = isqrt(MAX)+1

def Eratosthenes():
    Sieve = [0, 0]
    Sieve += [i for i in range(2, r)]
    for i in range(2, r):
        for j in range(i*i, r, i):
            if not Sieve[j]: continue
            Sieve[j] = 0
    return [prime_num for prime_num in range(2, r) if Sieve[prime_num]]

prime_Nums = Eratosthenes()

def is_prime(num):
    for prime in prime_Nums:
        if not num%prime and num//prime > 1: return False
        if prime > num: return True
    return True

for _ in range(int(input())):
    n = int(input())
    if n == 0 or n == 1: 
        print(2)
        continue
    x = n
    while True:
        if is_prime(x): 
            print(x)
            break
        x += 1 # 다음 소수값을 찾을때까지 1씩 더해줌