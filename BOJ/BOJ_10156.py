import sys
input = sys.stdin.readline
# [BOJ] 10156 과자 / 수학, 사칙연산
a, b, c = map(int, input().split())
if a * b >= c: print(a*b-c)
else: print(0)