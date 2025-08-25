from math import factorial
import sys
input = sys.stdin.readline
# [BOJ] 31048 Last Factorial Digit / 수학, 사칙연산
for _ in range(int(input())):
    print(factorial(int(input())) % 10)