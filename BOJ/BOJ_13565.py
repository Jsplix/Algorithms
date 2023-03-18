from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 13565 침투 / 그래프 이론, 그래프 탐색, BFS, DFS
m, n = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(m)]

queue = deque([])
for i in range(n):
    if grid[0][i] == '0': queue.append((i, 0))


visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx] and grid[ny][nx] == '0':
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))

bfs()
answer = False
for i in range(n):
    if visited[-1][i]: answer = True; break

if answer: print("YES")
else: print("NO")