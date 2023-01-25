import sys
input = sys.stdin.readline

# [BOJ] 1197 최소 스패닝 트리 / 최소 신장 트리(MST), 그래프 이론, 크루스칼

v, e = map(int, input().split())
edges = []
vertex = [ i for i in range(v+1)]
for _ in range(e):
    v1, v2, edge = map(int, input().split())
    edges.append((v1, v2, edge))

edges.sort(key=lambda x:x[2])

def find(x):
    if x != vertex[x]:
        vertex[x] = find(vertex[x])
    return vertex[x]

val = 0

for n1, n2, w in edges:
    root_1 = find(n1)
    root_2 = find(n2)
    if root_1 != root_2:
        if root_1 > root_2: vertex[root_1] = root_2
        else: vertex[root_2] = root_1
        val += w

print(val)