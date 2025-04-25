import sys
input = sys.stdin.readline
# [BOJ] 2406 안정적인 네트워크 / 그래프 이론, 최소 스패닝 트리(MST)
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa < pb: parent[pb] = pa
    else: parent[pa] = pb

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

adjacency = [list(map(int, input().split())) for _ in range(n)]

edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((adjacency[i][j], i+1, j+1))

edges.sort(key=lambda x: -x[0])
X, K = 0, []
while edges:
    weight, v, e = edges.pop()
    if v == 1 or e == 1: continue

    pv, pe = find(v), find(e)
    if pv != pe:
        X += weight
        K.append((v, e))
        union(pv, pe)

print(X, len(K))
for k in K:
    print(*k)