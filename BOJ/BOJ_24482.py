import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
# [BOJ] 24482 알고리즘 수업 - 깊이 우선 탐색 4 / 그래프 이론, 그래프 탐색, DFS, 정렬
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [-1 for _ in range(n+1)]

path = []
def dfs(start, idx):
    path.append(start)
    visited[start] = idx
    for vrtx in sorted(graph[start], reverse=True):
        if visited[vrtx] == -1:
            dfs(vrtx, idx+1)
dfs(r, 0)
print(*visited[1:], sep = '\n')