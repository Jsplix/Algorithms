import sys
input = sys.stdin.readline
# [BOJ] 13418 학교 탐방하기 / 그래프 이론, 최소 스패닝 트리(MST)
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b    

n, m = map(int, input().split())
up = [[] for _ in range(n+1)]
down = [[] for _ in range(n+1)]

edges = []
for _ in range(m+1):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort(key=lambda x: x[0])

# 오르막길 먼저 확인
parents = [i for i in range(n+1)]
up = 0
for i in range(m+1):
    weight, s, e = edges[i]
    if find(s) != find(e):
        union(s, e)
        up += weight

parents = [i for i in range(n+1)]
down = 0
for i in range(m, -1, -1):
    weight, s, e = edges[i]
    if find(s) != find(e):
        union(s, e)
        down += weight

result = (n-up)**2 - (n-down)**2
print(result)