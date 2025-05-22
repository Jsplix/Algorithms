import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 10282 해킹 / 그래프 이론, 최단 경로, 다익스트라
INF = 10**7+9
def dijkstra(v):
    global n
    dist = [INF for _ in range(n+1)]
    dist[v] = 0

    queue = deque([(0, v)])
    while queue:
        current_time, node = queue.popleft()
        for infection_time, next_node in graph[node]:
            new_time = current_time + infection_time
            if dist[next_node] > new_time:
                dist[next_node] = new_time
                queue.append((new_time, next_node))

    return dist

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for __ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    
    result = dijkstra(c)
    mx, count = -1, 0
    for i in range(1, len(result)):
        if result[i] > mx and result[i] != INF:
            mx = result[i]
        count += 1 if result[i] != INF else 0
    print(count, mx)