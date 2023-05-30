from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 17129 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유 / 그래프 이론, BFS
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(pos_x, pos_y, dist):
    global n, m
    queue = deque([(pos_x, pos_y, dist)])
    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and info_island[ny][nx] == 0:
                queue.append([nx, ny, d+1])
                info_island[ny][nx] = 2
            if 0 <= nx < m and 0 <= ny < n and info_island[ny][nx] >= 3:
                print("TAK", d+1, sep='\n')
                exit(0)
            
n, m = map(int, input().split())
info_island = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if info_island[i][j] == 2:
            bfs(j, i, 0)
print("NIE")