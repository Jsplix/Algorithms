import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def dfs(v, wei):
    for i in graph[v]:
        u, d = i
        if dist[u] == -1:
            dist[u] = dist[v] + d
            dfs(u, wei + d)
# 1(루트 노드)에서부터 가장 먼 노드 탐색
dist = [ -1 for _ in range(n + 1) ]
dist[1] = 0
dfs(1, 0)

# 위에서 찾은 가장 먼 거리의 노드에서부터 다시 가장 먼 노드를 찾음
max_dist = dist.index(max(dist))
dist = [ -1 for _ in range(n + 1) ]
dist[max_dist] = 0
dfs(max_dist, 0)
# 정답 출력
print(max(dist))