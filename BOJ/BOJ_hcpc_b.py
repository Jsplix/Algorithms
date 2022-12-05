from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [ False for _ in range(n + 1) ]
visited[0] = True
def bfs(idx):
    visited[idx] = True
    queue = deque([idx])

    while queue:
        x = queue.popleft()
        for v in graph[x]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

for i in range(1, n + 1):
    bfs(i)
    if False in visited:
        print("No")
        exit(0)
    else:
        visited = [ False for _ in range(n + 1) ]
        visited[0] = True
print("Yes")
