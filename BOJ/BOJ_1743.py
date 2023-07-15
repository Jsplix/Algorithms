from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1743 음식물 피하기 / 그래프 이론, 그래프 탐색, BFS, DFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(pos_x, pos_y):
    global n, m
    queue = deque([(pos_x, pos_y)])
    size = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < m and 0 <= ny < n) and path[ny][nx]:
                size += 1
                queue.append((nx, ny))
                path[ny][nx] = 0
    
    return size

n, m, k = map(int, input().split())
path = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    path[r-1][c-1] = 1

answer = -1
for i in range(n):
    for j in range(m):
        if path[i][j] == 1:
           answer = max(answer, bfs(j, i))
print(answer) 