from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 11779 최소비용 구하기 2 / 그래프 이론, 다익스트라
INF = int(1e9)
n = int(input()); m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, d, w = map(int, input().split())
    graph[s].append((d, w))
start, destination = map(int, input().split())
hist = [0 for _ in range(n+1)]
def dijkstra(start):
    dist = [INF for _ in range(n+1)]
    dist[start] = 0

    pq = []
    heappush(pq, (0, start)) # 가중치, 현재 노드

    while pq:
        v, c = heappop(pq)
        if dist[c] < v: continue
        for node, edge in graph[c]:
            weight = v + edge
            if weight < dist[node]:
                dist[node] = weight
                heappush(pq, (weight, node))
                hist[node] = c 
    
    return dist

d = dijkstra(start)

path = [destination]
now = destination
while now != start:
    now = hist[now]
    path.append(now)
path.reverse()

answer = d[destination]
print(answer, len(path), sep='\n')
print(*path)
