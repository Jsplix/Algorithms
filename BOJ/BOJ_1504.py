import sys
import heapq
input = sys.stdin.readline
# [BOJ] 1504 특정한 최단 경로 / 그래프 이론, 최단 경로, 다익스트라
# 1번 정점에서 N번 정점으로 이동.
# 임의의 v1, v2번 정점은 반드시 거쳐야 함.
# 1~v1~v2~N or 1~v2~v1~N 중 짧은 것 선택.

# 처음엔 10**6으로 설정했지만, 최대 간선 개수 2*(10**5) 와 최대 거리값 1000을 곱하면 2*(10**8)보다 커야함
INF = 987654321 
def dijkstra(start, destination):
    global n
    dist = [INF for _ in range(n+1)]
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        distance, now = heapq.heappop(pq)
        for next, next_distance in graph[now]:
            total = distance + next_distance
            if dist[next] > total:
                dist[next] = total
                heapq.heappush(pq, (total, next))
    
    return dist[destination]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

d1, d2 = dijkstra(1, v1), dijkstra(1, v2)
k = dijkstra(v1, v2)
g1, g2 = dijkstra(v1, n), dijkstra(v2, n)

result = min(d1+k+g2, d2+k+g1)
if result >= INF: print(-1)
else: print(result)