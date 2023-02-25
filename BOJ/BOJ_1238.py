from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = int(1e7)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# [BOJ] 1238 파티 / 그래프 이론, 다익스트라
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

def dijkstra(s):
    dist = [INF for _ in range(n+1)]
    dist[s] = 0
    priq = []
    heappush(priq, (0, s))

    while priq:
        val, cur = heappop(priq)
        if dist[cur] < val: continue
        for i in graph[cur]:
            weight = val + i[1]
            if weight < dist[i[0]]:
                dist[i[0]] = weight
                heappush(priq, (weight, i[0]))

    return dist

answer = 0
for i in range(1, n+1):
    g = dijkstra(i)
    r = dijkstra(x)
    answer = max(answer, r[i]+g[x])
print(answer)