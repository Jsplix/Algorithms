import sys
input = sys.stdin.readline
# [BOJ] 25238 가희와 방어율 무시 / 수학, 사칙연산
a, b = map(int, input().split())
a = a - a * (b / 100)

if a >= 100: print(0)
else: print(1)