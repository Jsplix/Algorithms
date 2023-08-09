from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 14940 쉬운 최단거리 / 그래프 탐색, 그래프 이론, BFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(pos_x, pos_y):
    global n, m
    queue = deque([(pos_x, pos_y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and ground[ny][nx] == 1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx, ny))
                ground[ny][nx] = -1

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 2:
            dist[i][j] = 0
            bfs(j, i)
        elif ground[i][j] == 0:
            dist[i][j] = 0
            
for i in range(n):
    print(*dist[i])