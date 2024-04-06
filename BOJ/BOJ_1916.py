import sys
import heapq
input = sys.stdin.readline
# [BOJ] 1916 최소비용 구하기 / 그래프 이론, 다익스트라, 최단 경로
def dijkstra(start, target):
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        weight, now = heapq.heappop(pq)
        if dist[now] < weight: continue # 이미 최단 거리인 경우
        for next_weight, next in traffic[now]: 
            total = next_weight + weight
            if total < dist[next]:
                dist[next] = total
                heapq.heappush(pq, (total, next))

n = int(input())
m = int(input())

traffic = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    traffic[s].append((w, e))

start, target = map(int, input().split())

MX = 10**8 + 5
dist = [MX for _ in range(n+1)]
dist[start] = 0

dijkstra(start, target)
print(dist[target])