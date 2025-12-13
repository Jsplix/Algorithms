import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2638 치즈 / 구현, 그래프 이론, 그래프 탐색, 격자 그래프, BFS, DFS, 시뮬레이션
def bfs(pr, pc):
    graph[pr][pc] = 2
    queue = deque([(pr, pc)])
    visited[pr][pc] = True

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if graph[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    graph[nr][nc] = 2

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

total = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            total += 1

bfs(0, 0) # Mark outside air with 2

time = 0
while total:
    temp = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                continue
            cnt = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 2:
                    cnt += 1
            
            if cnt >= 2:
                temp.append((i, j))
    
    for r, c in temp:
        graph[r][c] = 2
        bfs(r, c)
        total -=1 
    time += 1

print(time)