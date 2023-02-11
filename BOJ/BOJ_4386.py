import sys
input = sys.stdin.readline

# [BOJ] 4386 별자리 만들기 / 그래프 이론, 최소 신장 트리(MST)

n = int(input())
star_pos = [tuple(map(float, input().split())) for _ in range(n)]

vRoot = [i for i in range(n+1)]
edges = []
for i in range(n-1):
    for j in range(i+1, n):
        edges.append((i+1, j+1, ((star_pos[i][0]-star_pos[j][0])**2+(star_pos[i][1]-star_pos[j][1])**2)**0.5))
edges.sort(key=lambda x: x[2])

def find(x):
    if vRoot[x] != x: vRoot[x] = find(vRoot[x])
    return vRoot[x]

dist = 0
for edge in edges:
    v1, v2, w = edge
    v1_root = find(v1)
    v2_root = find(v2)

    if v1_root != v2_root:
        if v1_root < v2_root:
            vRoot[v2_root] = v1_root
        else:
            vRoot[v1_root] = v2_root
        dist += w

print(dist)