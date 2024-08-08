import sys
input = sys.stdin.readline
# [BOJ] 31090 2023은 무엇이 특별할까? / 수학, 구현, 사칙연산
for _ in range(int(input())):
    n = int(input())

    x = n % 100 if n % 100 != 0 else 100
    if (n + 1) % x == 0: print("Good")
    else: print("Bye")