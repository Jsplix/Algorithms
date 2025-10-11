import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# [BOJ] 13306 트리 / 자료 구조, 분리 집합(유니온 파인드), 오프라인 쿼리
def union(x, y):
    px = find(x)
    py = find(y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

N, Q = map(int, input().split())

parent = [i for i in range(N + 1)]
v = [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    k = int(input())
    v[i] = k

query = [list(map(int, input().split())) for _ in range(N - 1 + Q)]
query.reverse()

result = []
for qr in query:
    if qr[0] == 0:
        union(qr[1], v[qr[1]])
    else:
        px = find(qr[1])
        py = find(qr[2])
        result.append("YES" if px == py else "NO")

for r in result[::-1]:
    print(r)