import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 15591 MooTube (Silver) / 그래프 이론, 그래프 탐색, BFS, DFS
def BFS(node, r_value):
    global N

    queue = deque([node])
    visited = [0 for _ in range(N + 1)]
    visited[node] = 1

    while queue:
        curr = queue.popleft()

        for next, weight in graph[curr]:
            if weight >= r_value and not visited[next]:
                visited[next] = 1
                queue.append(next)
    
    return sum(visited) - 1

N, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for __ in range(Q):
    k, v = map(int, input().split())
    print(BFS(v, k))
