import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# [BOJ] 24479 알고리즘 수업 - 깊이 우선 탐색 1 / 그래프 이론, 그래프 탐색, DFS, 정렬
def dfs(now):
    global visited, graph, depth
    visited[now] = depth
    depth += 1
    for node in sorted(graph[now]):
        if visited[node]: continue
        dfs(node)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v); graph[v].append(u)

visited = [0 for _ in range(n+1)]
depth = 1
dfs(r)
print(*visited[1:], sep='\n')