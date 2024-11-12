import sys
from collections import defaultdict
input = sys.stdin.readline
# [BOJ] 2358 평행선 / 자료 구조, 정렬, 해시 사용한 집합과 맵
n = int(input())

x_pos = defaultdict(list)
y_pos = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    x_pos[x].append(y)
    y_pos[y].append(x)

result = 0
for k in x_pos:
    if len(x_pos[k]) >= 2:
        result += 1
for k in y_pos:
    if len(y_pos[k]) >= 2:
        result += 1
print(result)