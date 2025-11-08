import sys
input = sys.stdin.readline
# [BOJ] 1774 우주신과의 교감 / 그래프 이론, MST
def union(px, py):
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

N, M = map(int, input().split())

p = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]

edges = []
for i in range(N):
    for j in range(i + 1, N):
        distance = ((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2) ** 0.5
        edges.append((i + 1, j + 1, distance))

edges.sort(key=lambda x:(x[2]))

for i in range(M):
    a, b = map(int, input().split())
    pa = find(a)
    pb = find(b)

    union(pa, pb)

result = 0.0
for edge in edges:
    pi = find(edge[0])
    pj = find(edge[1])

    if pi != pj:
        union(pi, pj)
        result += edge[2]

print("%.2f" % result)