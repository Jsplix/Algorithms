import sys
input = sys.stdin.readline
# [BOJ] 17356 욱 제 / 수학, 사칙연산
a, b = map(int, input().split())
m = (b - a) / 400
p = 1 / (1 + 10**m)
print(p)