import sys
input = sys.stdin.readline
# [BOJ] 10423 전기가 부족해 / 그래프 이론, 최소 스패닝 트리
def find(v):
    if parent[v] != v: return find(parent[v])
    return parent[v]

def union(s, e):
    ps, pe =  find(s), find(e)
    if ps in generators and pe in generators:
        return False
    elif ps in generators:
        parent[pe] = ps
    elif pe in generators:
        parent[ps] = pe
    else:
        if ps < pe: parent[pe] = ps
        else: parent[ps] = pe
    return True

n, m, k = map(int, input().split())
generators = set(map(int, input().split()))
parent = [i for i in range(n+1)]

# len(generators)의 수만큼 MST를 만들어주면 됨.
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort(reverse=True)

result = 0
while edges:
    weight, v1, v2 = edges.pop()
    pv1, pv2 = find(v1), find(v2)
    if pv1 != pv2:
        if union(v1, v2):
            result += weight
print(result)