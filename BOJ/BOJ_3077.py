import sys
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 3077 임진왜란 / 자료 구조, 브루트포스, 해시 사용 집합과 맵
n = int(input())
d = dict(zip(input().split(), [v for v in range(n)]))
answer = list(input().split())

count = 0
possible = combinations(answer, 2)
for p in possible:
    if d[p[0]] < d[p[1]]: count += 1

print("%d/%d" % (count, (n*(n-1))/2))