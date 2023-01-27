# [BOJ] 11725 트리의 부모 찾기 / DFS, 트리, 그래프 이론
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [ 0 for _ in range(n + 1) ]
p = [0 for _ in range(n + 1)] # recording parent node
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

def dfs(idx):
    if graph[idx] == [p[idx]]:
        return
    
    for v in graph[idx]:
        if not visited[v]:
            p[v] = idx # if child node exist, record parent node to list p
            visited[v] = 1
            dfs(v) # checking child node for sub node
dfs(1)
print('\n'.join(map(str, p[2:])))