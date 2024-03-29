import sys
import heapq
input = sys.stdin.readline
# [BOJ] 18352 특정 거리의 도시 찾기 / 그래프 이론, 그래프 탐색, 다익스트라, BFS, 최단 경로
def dijkstra(start):
    global n
    dist = [(10**6 + 1) for _ in range(n + 1)]
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        weight, now = heapq.heappop(pq)
        if dist[now] < weight: continue
        for next in graph[now]:
            if dist[next] > weight + 1:
                dist[next] = weight + 1
                heapq.heappush(pq, (dist[next], next))
    
    return dist

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = []
for i, w in enumerate(dijkstra(x)):
    if w == k: answer.append(i)

if answer: print(*answer, sep='\n')
else: print(-1)