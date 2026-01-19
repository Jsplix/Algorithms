import sys
input = sys.stdin.readline
# [BOJ] 28812 Доставка / 수학, 구현, 사칙연산
N, C = map(int, input().split())
mn = 10000000
for _ in range(N):
    p, v, k = map(int, input().split())
    mn = min(mn, p + v + C * k)
print(mn)