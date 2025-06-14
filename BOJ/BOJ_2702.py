import sys
import math
input = sys.stdin.readline
# [BOJ] 2702 초6 수학 / 수학, 브루트포스, 정수론, 사칙연산
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(math.lcm(a, b), math.gcd(a, b))