from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 17086 아기 상어 2 / 그래프 이론, 그래프 탐색, BFS, 브루트 포스
n, m = map(int, input().split())
space = [[*map(int, input().split())] for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if space[i][j]: queue.append((j, i))

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]
# visited = [[0 for _ in range(m)] for _ in range(n)]

def bfs():    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not space[ny][nx]:
                space[ny][nx] = space[y][x] + 1
                queue.append((nx, ny))

bfs()
mx = -1
for i in range(n):
    for j in range(m):
        if space[i][j] > mx: mx = space[i][j]
print(mx-1)