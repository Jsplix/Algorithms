import sys
import heapq
input = sys.stdin.readline
# [BOJ] 20183 골목 대장 호석 - 효율성 2 / 그래프 이론, 최단 경로, 다익스트라, 이분 탐색, 매개 변수 탐색
def dijkstra(start, target, limit):
    global A, B, C
    INF = 10 ** 14 + 14
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        w, v = heapq.heappop(pq)

        if w > distance[v]: continue 
        for nv, nw in graph[v]:
            tw = w + nw

            if tw < distance[nv] and nw <= limit:
                distance[nv] = tw
                heapq.heappush(pq, (tw, nv))

    return distance[target] <= C


N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cost = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    cost.append(c)

cost.sort()
left, right = 0, M - 1
result = 10 ** 9 + 9
while left <= right:
    mid = (left + right) // 2

    if dijkstra(A, B, cost[mid]):
        right = mid - 1
        result = min(result, cost[mid])
    else:
        left = mid + 1

print(result if result != (10 ** 9 + 9) else -1)