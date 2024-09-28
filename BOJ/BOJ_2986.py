import sys
input = sys.stdin.readline
# [BOJ] 2986 파스칼 / 수학, 정수론
n = int(input())

if n == 1: print(0)
else:
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if not n % i:
            divisors.append(i)
            if i ** 2 != n:
                divisors.append(n // i)
    divisors.sort()
    print(n-divisors[-2])