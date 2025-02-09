import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 1303 전쟁 - 전투 / 그래프 이론, 그래프 탐색, BFS, DFS
def bfs(x, y, color):
    global n, m
    queue = deque([(y, x)])
    visited[y][x] = 1
    
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    count = 1

    while queue:
        ty, tx = queue.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]

            if not (0 <= nx < n and 0 <= ny < m): continue

            if not visited[ny][nx] and wars[ny][nx] == color:
                queue.append((ny, nx))
                count += 1
                visited[ny][nx] = 1
    
    return count ** 2

n, m = map(int, input().split())
wars = [list(input().rstrip()) for _ in range(m)]
visited = [[0 for _ in range(n)] for __ in range(m)]

w, b = 0, 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            score = bfs(j, i, wars[i][j])
            if wars[i][j] == 'W':
                w += score
            else:
                b += score

print(w, b) 