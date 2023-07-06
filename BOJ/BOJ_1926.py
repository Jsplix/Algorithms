from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1926 그림 / 그래프 이론, 그래프 탐색, BFS, DFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(pos_x, pos_y):
    global n, m
    queue = deque([(pos_x, pos_y)])
    picture[pos_y][pos_x] = 0
    area = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and picture[ny][nx] == 1:
                queue.append((nx, ny))
                picture[ny][nx] = 0
                area += 1
    return (1, area)

picture = []
n, m = map(int, input().split())
for _ in range(n):
    picture.append(list(map(int, input().split())))

k, s = 0, 0
cnt, max_size = 0, 0
for i in range(n):
    for j in range(m):
        if picture[i][j] == 1:
            k, size = bfs(j, i)
            cnt += k
            max_size = max(size, max_size)

print(cnt, max_size, sep='\n')