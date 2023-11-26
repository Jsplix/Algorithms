from math import comb
import sys
input = sys.stdin.readline
# [BOJ] 24723 녹색거탑 / 수학, 사칙연산
n = int(input())
possible = 0
for i in range(n+1): possible += comb(n, i)
print(possible)