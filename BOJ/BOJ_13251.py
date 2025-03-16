import sys
from math import comb
input = sys.stdin.readline
# [BOJ] 13251 조약돌 꺼내기 / 수학, 조합론, 확률론
m = int(input())
stones = list(map(int, input().split()))
k = int(input())

if m == 1 or k == 1: print(1.0)
else:
    n = sum(stones)
    q = comb(n, k)
    p = 0
    for s in stones:
        p += comb(s, k)
    print(p/q)