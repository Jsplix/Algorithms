import sys
import heapq
input = sys.stdin.readline
# [BOJ] 4485 녹색 옷 입은 애가 젤다지? / 그래프 이론, 다익스트라, 최단 경로
def dijkstra():
    global n, idx, dist
    pq = []
    heapq.heappush(pq, (cave[0][0], 0, 0)) # 도둑루피, x좌표, y좌표
    dist[0][0] = 0

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while pq:
        rupee, x, y = heapq.heappop(pq)
        
        if x == n-1 and y == n-1:
            print(f"Problem {idx}: {dist[y][x]}")
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if rupee + cave[ny][nx] < dist[ny][nx]:
                    dist[ny][nx] = rupee + cave[ny][nx]
                    heapq.heappush(pq, (dist[ny][nx], nx, ny))

idx = 1
while True:
    n = int(input())
    if n == 0: break

    MX = 10**6 + 7
    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [list(MX for _ in range(n)) for _ in range(n)]

    dijkstra()
    idx += 1