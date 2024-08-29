import sys
input = sys.stdin.readline
# [BOJ] 20955 민서의 응급 수술 / 자료 구조, 그래프 이론, 트리, 분리 집합
def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]

def union(v1, v2):
    p1, p2 = find(v1), find(v2)

    if p1 < p2: parent[p2] = p1
    else: parent[p1] = p2

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
answer = 0
for _ in range(m):
    u, v = map(int, input().split())
    if find(u) == find(v):
        answer += 1
    union(u, v)

for i in range(1, n):
    if find(i) != find(i+1):
        union(i, i+1)
        answer += 1
print(answer)