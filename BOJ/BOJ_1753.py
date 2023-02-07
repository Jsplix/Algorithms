from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 1753 최단경로 / 그래프 이론, 다익스트라
# 다익스트라 - 하나의 정점에서 다른 정점들까지의 최소 거리
# 플로이드 와샬 - 모든 정점의 최단 거리
s, e = map(int, input().split())
p = int(input())
INF = int(1e7)
graph = [[] for _ in range(s+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [INF for _ in range(s+1)]
dist[p] = 0
pri_q = []
heappush(pri_q, (0, p))

while pri_q:
    d, cur = heappop(pri_q)
    if dist[cur] < d: continue
    for i in graph[cur]:
        val = d + i[1]
        if val < dist[i[0]]:
            dist[i[0]] = val
            heappush(pri_q, (val, i[0]))

for i in range(1, s+1):
    if dist[i] == INF: print('INF')
    else: print(dist[i])
