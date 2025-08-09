import sys
import math
input = sys.stdin.readline
# [BOJ] 30802 웰컴 키트 / 수학, 구현, 사칙연산
n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

a, b, c = 0, n // p, n % p
for sz in size:
    a += math.ceil(sz / t)

print(a)
print(b, c)