import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 2015 수들의 합 4 / 자료 구조, 누적합, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵
n, k = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
d[0] = 1
sm, result = 0, 0
for a in A:
    sm += a
    if sm - k in d:
        result += d[sm - k]
    d[sm] += 1
print(result)