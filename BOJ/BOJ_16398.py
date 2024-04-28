import sys
input = sys.stdin.readline
# [BOJ] 16398 행성 연결 / 그래프 이론, 최소 스패닝 트리, 크루스칼
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
edges = []

for r in range(n):
    for c in range(r + 1, n):
        edges.append((cost[r][c], r, c))

edges.sort()
vertex = [i for i in range(n+1)]

def find(x):
    if x != vertex[x]:
        vertex[x] = find(vertex[x])
    return vertex[x]

def union(s, e):
    s = find(s)
    e = find(e)

    if s < e: vertex[e] = s
    else: vertex[s] = e

answer = 0
for weight, v1, v2 in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        answer += weight

print(answer)