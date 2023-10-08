import sys
input = sys.stdin.readline
# [BOJ] 30204 병영외 급식 / 수학, 애드 혹, 사칙연산
n, x = map(int, input().split())
p = list(map(int, input().split()))

if sum(p) % x == 0: print(1)
else: print(0)