import sys
input = sys.stdin.readline
# [BOJ] 24314 알고리즘 수업 - 점근적 표기 2 / 수학
a = list(map(int, input().split()))
c = int(input())
n = int(input())
if c*n <= a[0]*n+a[1] and c <= a[0]: print(1)
else: print(0)