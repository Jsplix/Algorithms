import sys
input = sys.stdin.readline
# [BOJ] 2875 대회 or 인턴 / 수학, 구현, 사칙연산
n, m, k = map(int, input().split())

while k:
    if n // 2 >= m:
        k -= 1
        n -= 1
    else:
        k -= 1
        m -= 1

print(min(n // 2, m))