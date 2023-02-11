from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 24445 알고리즘 수업 - 너비 우선 탐색 2 / 그래프 이론, 그래프 탐색, 정렬, BFS
def bfs(r):
    queue = deque([r])
    visited[r] = 1
    c = 1
    while queue:
        s = queue.popleft()
        for x in graph[s]:
            if not visited[x]:
                visited[x] = c + 1
                queue.append(x)
                c += 1

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

bfs(r)

print(*visited[1:], sep='\n')