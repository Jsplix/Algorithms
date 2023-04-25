from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 24444 알고리즘 수업 - 너비 우선 탐색 1 / 그래프 이론, BFS, 정렬
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]
def bfs(start):
    seq = 1
    queue = deque([start])
    visited[start] = seq
    seq += 1    
    while queue:
        v = queue.popleft()
        for node in sorted(graph[v]):
            if not visited[node]:
                queue.append(node)
                visited[node] = seq
                seq += 1
bfs(r)
print(*visited[1:], sep='\n')