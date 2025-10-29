import sys
input = sys.stdin.readline
# [BOJ] 1976 여행 가자 / 자료 구조, 그래프 이론, 그래프 탐색, 분리 집합
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

N = int(input())
M = int(input())

parent = [i for i in range(N)]

for i in range(N):
    trip = list(map(int, input().split()))
    for j in range(N):
        if trip[j]: 
            union(i, j)

sequence = list(map(int, input().split()))
root = parent[sequence[0] - 1]
for i in range(1, M):
    if parent[sequence[i] - 1] != root:
        print("NO")
        exit()
print("YES")