import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
# [BOJ] 1717 집합의 표현 / 자료 구조, 분리 집합
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x, y):
    u = find(x)
    v = find(y)

    if u < v: parent[v] = u
    else: parent[u] = v

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    elif a == 1:
        if find(b) == find(c): print("YES")
        else: print("NO")