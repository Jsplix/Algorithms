from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 14716 현수막 / 그래프 이론, 그래프 탐색, DFS, BFS
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

def bfs(pos_x, pos_y):
    global m, n
    queue = deque([(pos_x, pos_y)])
    placard[pos_y][pos_x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and placard[ny][nx] == 1:
                placard[ny][nx] = 0
                queue.append((nx, ny))
    return 1
m, n = map(int, input().split())
placard = [list(map(int, input().split())) for _ in range(m)]

answer = 0
for i in range(m):
    for j in range(n):
        if placard[i][j] == 1:
            answer += bfs(j, i)

print(answer)