import sys
input = sys.stdin.readline
# [BOJ] 24337 가희와 탑 / 그리디, 해 구성하기
n, a, b = map(int, input().split())

buildings = []
for h1 in range(1, a):
    buildings.append(h1)
buildings.append(max(a, b))

for h2 in range(b-1, 0, -1):
    buildings.append(h2)

if len(buildings) > n: print(-1)
else:
    for i in range(n-len(buildings)):
        buildings.insert(1, 1)
    print(*buildings)