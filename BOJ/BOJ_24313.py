import sys
input = sys.stdin.readline
# [BOJ] 24313 알고리즘 수업 - 점근적 표기 1 / 수학
a, b = map(int, input().split())
c = int(input())
n = int(input())

if (a*n+b <= c*n and a <= c): print(1)
else: print(0)