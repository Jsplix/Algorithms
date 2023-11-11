from math import gcd
import sys
input = sys.stdin.readline
# [BOJ] 1735 분수 합 / 수학, 정수론, 유클리드 호제법
a, b = map(int, input().split())
c, d = map(int, input().split())

p, q = d*b, a*d + c*b
g = gcd(p, q)
print(q//g, p//g)