import sys
input = sys.stdin.readline
# [BOJ] 13225 Divisors / 수학, 구현, 브루트포스, 사칙연산
for _ in range(int(input())):
    cnt = 0
    n = int(input())
    for i in range(1, n + 1):
        if n % i == 0: cnt += 1
    print(n, cnt)