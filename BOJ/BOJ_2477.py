# BOJ_2477 참외밭
import sys
input = sys.stdin.readline

n = int(input())
h, w = [], []
t = []
for _ in range(6):
    dir, dist = map(int, input().split())
    if dir == 1 or dir == 2:
        w.append(dist)
    if dir == 3 or dir == 4:
        h.append(dist)
    t.append(dist)
big = max(h) * max(w)

w_idx = t.index(max(w))
h_idx = t.index(max(h))

sh = abs(t[h_idx - 1] - t[(h_idx - 5 if h_idx == 5 else h_idx + 1)])
sw = abs(t[w_idx - 1] - t[(w_idx - 5 if w_idx == 5 else w_idx + 1)])

print(n * (big - (sh * sw)))