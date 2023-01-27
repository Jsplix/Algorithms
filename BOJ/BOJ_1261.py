from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 1261 알고스팟 / 다익스트라, BFS, 그래프 이론
n, m = map(int, input().split())
maze = []
for i in range(m):
    maze.append(list(map(int, input().rstrip())))
visited = [[-1 for _ in range(n)] for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    if maze[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft((nx, ny)) # 왼쪽으로 추가해서 우선적으로 처리하도록 한다.
                    elif maze[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
bfs()
print(visited[m - 1][n - 1])