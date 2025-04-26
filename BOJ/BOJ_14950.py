import sys
input = sys.stdin.readline
# [BOJ] 14950 정복자 / 그래프 이론, 최소 스패닝 트리(MST)
def find(x):
    if parent[x] != x: return find(parent[x])
    return parent[x]

n, m, t = map(int, input().split())
parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])
edges.sort(key=lambda x: x[0])

count = 0
result = 0
for cost, v1, v2 in edges:
    p1, p2 = find(v1), find(v2)

    if p1 != p2:
        if p1 < p2:
            parent[p2] = p1
        else:
            parent[p1] = p2

        count += 1
        result += cost

for i in range(count-1):
    result += (i+1) * t
print(result)