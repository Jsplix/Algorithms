import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# [BOJ] 24480 알고리즘 수업 - 깊이 우선 탐색 2 / 그래프 이론, 그래프 탐색, 정렬, DFS
def dfs(idx, path: list):
    global n
    if len(path) == n:
        print(*path, sep='\n')
        exit(0)
    
    for node in sorted(graph[idx], reverse=True):
        if not visited[node]:
            visited[node] = len(path) + 1
            path.append(node)
            dfs(node, path)
            

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(n+1)]
visited[r] = 1
dfs(r, [r])
print(*visited[1:], sep='\n')