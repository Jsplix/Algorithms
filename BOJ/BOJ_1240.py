import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
# [BOJ] 1240 노드사이의 거리 / 그래프 이론, 그래프 탐색, 트리, BFS, DFS
def dfs(now, target, dist):
    global n, flag
    if now == target:
        print(dist)
        flag = True
        return
    
    for node, weight in trees[now]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, target, dist + weight)
            visited[node] = 0
            if flag: break
    
n, m = map(int, input().split())
trees = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    trees[a].append((b, w))
    trees[b].append((a, w))

for i in range(m):
    v1, v2 = map(int, input().split())
    visited = [0 for _ in range(n+1)]
    visited[v1] = 1
    flag = False
    dfs(v1, v2, 0)