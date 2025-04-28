import sys
import heapq
input = sys.stdin.readline
# [BOJ] 14461 소가 길을 건너간 이유 7 / 그래프 이론, 최단 경로, 다익스트라
INF = sys.maxsize

def get_distance(x, y):
    return abs(n-1-y) + abs(n-1-x)

def dijkstra(n, t):
    dist = [[INF for _ in range(n)] for __ in range(n)]
    dist[0][0] = 0

    pq = []
    heapq.heappush(pq, [0, 0, 0]) # cost, y, x
    result = INF
    while pq:
        cost, y, x = heapq.heappop(pq)

        if dist[y][x] < cost: continue

        to_destination = get_distance(x, y)
        if to_destination <= 2:
            result = min(result, cost + to_destination*t)

        for i in range(16):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = 3*t + grounds[ny][nx]

                if dist[ny][nx] > cost + new_cost:
                    dist[ny][nx] = cost + new_cost
                    heapq.heappush(pq, [cost + new_cost, ny, nx])

    return result


# 3칸씩 움직이는 경우의 dx, dy (ex. →→←(0, 1), →→↓(-1, 2))
dx = [-1, 0, 1, 0, -2, -1, 1, 2, 2, 1, -1, -2, -3, 0, 3, 0]
dy = [0, -1, 0, 1, -1, -2, -2, -1, 1, 2, 2, 1, 0, -3, 0, 3]

n, t = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(n)]

print(dijkstra(n, t))