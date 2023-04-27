import sys
input = sys.stdin.readline
# [BOJ] 27959 초코바 / 수학, 사칙연산
n, m = map(int, input().split())

if 100*n >= m: print("Yes")
else: print("No")