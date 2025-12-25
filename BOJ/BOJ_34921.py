import sys
input = sys.stdin.readline
# [BOJ] 34921 덕후 / 수학, 사칙연산
a, t = map(int, input().split())
p = 10 + 2 * (25 - a + t)
print(p if p >= 0 else 0)