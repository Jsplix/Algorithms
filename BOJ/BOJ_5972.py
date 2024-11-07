import sys
import heapq
input = sys.stdin.readline
# [BOJ] 5972 택배 배송 / 그래프 이론, 최단 경로, 다익스트라
INF = 5*(10**7)+7

def dijkstra(start, destination):
    global n
    distance = [INF for _ in range(n+1)]

    pq = []
    heapq.heappush(pq, [0, start])
    distance[start] = 0

    while pq:
        cost, now = heapq.heappop(pq)
        for next, new_cost in graph[now]:
            if distance[now] + new_cost < distance[next]:
                distance[next] = distance[now] + new_cost
                heapq.heappush(pq, [distance[next], next])

    return distance[destination]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra(1, n))