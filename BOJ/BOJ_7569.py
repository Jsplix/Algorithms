from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 7569 토마토 / 그래프 이론, 그래프 탐색, BFS
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((k, j, i))

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if box[nz][ny][nx] == -1: continue
                if not box[nz][ny][nx]: 
                    box[nz][ny][nx] = box[z][y][x] + 1
                    queue.append((nx, ny, nz))

flag = True
cnt = 0
bfs()
for i in range(h):
    if not flag: break
    for j in range(n):
        if not flag: break
        for k in range(m):
            if box[i][j][k] == 0:
                flag = False
                print(-1)
                break
        cnt = max(cnt, max(box[i][j]))
if flag: print(cnt - 1)