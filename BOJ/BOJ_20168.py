import sys
import heapq
input = sys.stdin.readline
# [BOJ] 20168 골목 대장 호석 - 기능성 / 그래프 이론, 브루트포스, 최단 경로, 다익스트라, 백트래킹
MAX = 10**6
def dijkstra(s, e):
    global money, answer
    distance = [MAX for _ in range(n+1)]
    distance[s] = 0

    pq = []
    visited = [[0 for _ in range(n+1)] for __ in range(n+1)]
    heapq.heappush(pq, (0, 0, start))

    while pq:
        mx, w, v =  heapq.heappop(pq)
        if w > money: continue
        if distance[v] < w: continue
        for next, weight in graph[v]:
            new_weight = weight + w
            if new_weight > money or visited[v][next]: continue
            elif next == e:
                answer = min(answer, max(mx, weight))

            visited[v][next] = 1
            heapq.heappush(pq, (max(weight, mx), new_weight, next))

n, m, start, destination, money = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

answer = MAX
dijkstra(start, destination)
print(answer if answer != MAX else -1)