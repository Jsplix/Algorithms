from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 2146 다리 만들기 / 그래프 이론, 그래프 탐색, BFS
n = int(input())
visited = [ [0 for _ in range(n)] for _ in range(n) ]
island = [ list(map(int, input().split())) for _ in range(n) ]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(i, j, c):
    island_pos.append([])
    queue = deque([(i, j)])
    visited[i][j] = c
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if island[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = c
island_pos = []
chk = 1
for i in range(n):
    for j in range(n):
        if island[i][j] == 1 and not visited[i][j]:
            bfs(i, j, chk)
            chk += 1
        if visited[i][j]:
            island_pos[visited[i][j] - 1].append((i, j))

def gap(val):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if island[nx][ny] == 1 and visited[nx][ny] != val:
                return l[x][y] - 1
            if island[nx][ny] == 0 and l[nx][ny] == 0:
                l[nx][ny] = l[x][y] + 1
                q.append((nx, ny))            

min_gap = int(1e3)
for i in range(1, chk):
    q = deque([])
    l = [ [0] * n for _ in range(n) ]
    for j in range(n):
        for k in range(n):
            if island[j][k] == 1 and visited[j][k] == i:
                q.append((j, k))
                l[j][k] = 1
    res = gap(i)
    min_gap = min(min_gap, res)

print(min_gap)