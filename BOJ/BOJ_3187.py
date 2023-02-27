from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 3187 양치기 꿍 / 그래프 이론, 그래프 탐색, BFS, DFS
r, c = map(int, input().split())
space = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[0 for _ in range(c)] for _ in range(r)]

def bfs(pos_x, pos_y):
    queue = deque([(pos_x, pos_y)])
    visited[pos_y][pos_x] = 1
    wolf, sheep = 0, 0
    if space[pos_y][pos_x] == 'v': wolf += 1
    else: sheep += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and space[ny][nx] != '#' and not visited[ny][nx]:
                if space[ny][nx] == 'k': sheep += 1
                if space[ny][nx] == 'v': wolf += 1
                queue.append((nx, ny))
                visited[ny][nx] = 1
    if wolf < sheep: wolf = 0
    else: sheep = 0
    return (sheep, wolf)

s, w = 0, 0
for i in range(r):
    for j in range(c):
        if (space[i][j] == 'v' or space[i][j] == 'k') and not visited[i][j]: # v = 늑대 / k = 양
            a, b = bfs(j, i)
            s += a
            w += b
print(s, w)