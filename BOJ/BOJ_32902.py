import sys
input = sys.stdin.readline
# [BOJ] 32902 Chips / 수학, 사칙연산
n, k = map(int, input().split())
print(k+1, n*k+1)