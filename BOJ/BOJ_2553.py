import sys
import math
input = sys.stdin.readline
# [BOJ] 2553 마지막 팩토리얼 수 / 수학, 정수론
x = int(input())
s = str(math.factorial(x))

for i in range(len(s)-1, -1, -1):
    if s[i] != '0':
        print(s[i])
        break