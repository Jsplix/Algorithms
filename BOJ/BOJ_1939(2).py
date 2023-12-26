from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1939 중량제한 / 자료 구조, 그래프 이론, 그래프 탐색, 다익스트라, BFS, 이분 탐색, 분리 집합
def bfs(start, end, weight):
    visited[start] = 1
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for new_node, new_weight in graph[node]:
            if not visited[new_node] and weight <= new_weight:
                queue.append(new_node)
                visited[new_node] = 1
    
    return False

inf = int(1e9) + 1
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))
f1, f2 = map(int, input().split())

for i in range(1, n+1):
    graph[i].sort(reverse=True)

left, right = 1, int(1e9)
while left <= right:
    visited = [0 for _ in range(n+1)]
    mid = (left + right) // 2
    
    if bfs(f1, f2, mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)