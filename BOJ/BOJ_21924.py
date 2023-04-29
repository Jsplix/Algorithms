import sys
input = sys.stdin.readline
# [BOJ] 21924 도시 건설 / 그래프 이론, 최소 스패닝 트리
def find(v):
    if k[v] == v: return v
    else: k[v] = find(k[v])
    return k[v]

def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    k[max(v1, v2)] = min(v1, v2)

def check(v1, v2):
    return find(v1) == find(v2)

n, m = map(int, input().split())
cities = []
total = 0
k = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cities.append((c, a, b))
    total += c
cities.sort()

val = 0
for cost, v1, v2 in cities:
    if not check(v1, v2):
        val += cost
        union(v1, v2)

chk = 0
for i in range(1, n+1):
    if k[i] == i:
        chk += 1

if chk >= 2: print(-1)
else: print(total - val)