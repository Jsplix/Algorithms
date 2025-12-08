from math import ceil
import sys
input = sys.stdin.readline
# [BOJ] 34891 MT 준비 / 수학, 사칙연산
n, m = map(int, input().split())
print(ceil(n / m))