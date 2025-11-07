import sys
input = sys.stdin.readline
# [BOJ] 6497 전력난 / 그래프 이론, 최소 스패닝 트리(MST)
def union(px, py):
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

while True:
    M, N = map(int, input().split())

    if not N and not M: break

    parent = [i for i in range(M)]
    total_cost = 0

    edges = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        total_cost += z
        edges.append([x, y, z])

    edges.sort(key=lambda x:(x[2]))

    min_cost = 0
    for edge in edges:
        s, e, w = edge

        ps = find(s)
        pe = find(e)

        if ps != pe:
            min_cost += w
            union(ps, pe)

    result = total_cost - min_cost
    print(result)