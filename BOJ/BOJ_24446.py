import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 24446 알고리즘 수업 - 너비 우선 탐색 3 / 그래프 이론, 그래프 탐색, BFS
def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[now] + 1


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1 for _ in range(n+1)]
bfs(r)

print(*visited[1:], sep='\n')