import sys
input = sys.stdin.readline
# [BOJ] 10480 Oddities / 수학, 구현, 사칙연산
for _ in range(int(input())):
    x = int(input())
    if x % 2: print(x, "is odd")
    else: print(x, "is even")