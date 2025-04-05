import sys
import math
input = sys.stdin.readline
# [BOJ] 30993 자동차 주차 / 수학, 조합론
n, a, b, c = map(int, input().split())
result = math.comb(n, a) * math.comb(n-a, b)
print(result)