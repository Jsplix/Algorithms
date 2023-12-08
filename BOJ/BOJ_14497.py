from heapq import heappop, heappush
import sys
input = sys.stdin.readline
# [BOJ] 14497 주난의 난(難) / 그래프 이론, 그래프 탐색, 다익스트라, 최단 경로, 0-1 BFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(pos_x, pos_y, c):
    global n, m
    heap = []
    heappush(heap, (0, pos_x, pos_y))

    while heap:
        k, x, y = heappop(heap)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
                if graph[ny][nx] == '#':
                    return k+1
                elif graph[ny][nx] == '1':
                    visited[ny][nx] = 1
                    heappush(heap, (k+1, nx, ny))
                else:
                    visited[ny][nx] = 1
                    heappush(heap, (k, nx, ny))

n, m = map(int, input().split())
position = list(map(int, input().split()))
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for __ in range(n)]
visited[position[0]-1][position[1]-1] = 1

print(bfs(position[1]-1, position[0]-1, 0))