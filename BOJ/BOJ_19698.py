import sys
input = sys.stdin.readline
# [BOJ] 19698 헛간 청약 / 수학, 사칙연산
n, w, h, l = map(int, input().split())
a = w // l
b = h // l

if n > a*b:
    print(a*b)
else:
    print(n)