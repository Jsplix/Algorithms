import sys
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 28215 대피소 / 구현, 브루트포스, 시뮬레이션
N, K = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(N)]

safe_house = list(combinations(set(range(N)), K))
mn = 200007

for sh in safe_house:
    mx = 0
    for i in range(N):
        if i in sh: continue
        tmn = 200007
        for h in sh:
            tmn = min(abs(pos[h][0] - pos[i][0]) + abs(pos[h][1] - pos[i][1]), tmn)
        mx = max(mx, tmn)
    mn = min(mn, mx)

print(mn)