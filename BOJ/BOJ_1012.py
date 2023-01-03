from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1012 유기농 배추 / BFS, 그래프 탐색, 그래프 이론
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(pos_x, pos_y):
    queue = deque([(pos_x, pos_y)])
    visited[pos_y][pos_x] = 1
    c = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and farm[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = 1
    c += 1
    return c

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        farm[b][a] = 1
    chk = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1 and not visited[i][j]:
                chk += bfs(j, i)
    print(chk)