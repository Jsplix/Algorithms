import sys
import math
input = sys.stdin.readline
# [BOJ] 31798 단원평가 / 수학, 사칙연산
a, b, c = map(int, input().split())

if a == 0:
    a = c**2 - b
    print(a)
elif b == 0:
    b = c**2 - a
    print(b)
elif c == 0:
    c = a + b
    c = int(math.sqrt(c))
    print(c)