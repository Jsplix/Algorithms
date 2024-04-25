import sys
import heapq
input = sys.stdin.readline
# [BOJ] 22865 가장 먼 곳 / 그래프 이론, 다익스트라, 최단 경로
INF = 10**9 + 7
def dijkstra(start):
    global n, a, b, c
    dist = [INF for _ in range(n+1)]
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        now_distance, now = heapq.heappop(pq)
        if dist[now] < now_distance:
            continue
        for next, next_distance in graph[now]:
            new_distance = now_distance + next_distance
            if dist[next] > new_distance:
                dist[next] = new_distance
                heapq.heappush(pq, (new_distance, next))

    return dist

n = int(input())
a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

ret = [dijkstra(a), dijkstra(b), dijkstra(c)]
answer = [-1]
for i in range(1, n+1):
    mn_dist = min(ret[0][i], ret[1][i], ret[2][i])
    answer.append(mn_dist)

mx = max(answer)
print(answer.index(mx))