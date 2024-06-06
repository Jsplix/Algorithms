from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1707 이분 그래프 / 그래프 이론, 그래프 탐색, BFS, DFS, 이분 그래프
def bfs(idx, colors):
    queue = deque([idx])
    visited[idx] = colors

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = -1 * visited[v]
            elif visited[i] == visited[v]:
                return False
    return True
    
K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    graph = [ [] for _ in range(V + 1) ]
    visited = [0] * (V + 1)

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, V + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if not result:
                break
    print("YES" if result else "NO")