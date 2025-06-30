import sys
input = sys.stdin.readline
# [BOJ] 34027 제곱 수? / 수학, 구현, 사칙연산
for _ in range(int(input())):
    n = int(input())
    if n == (int(n**0.5))**2: print(1)
    else: print(0)