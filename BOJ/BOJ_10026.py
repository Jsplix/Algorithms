from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 10026 적록색약 / 그래프 이론, 그래프 탐색, BFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(pos_x, pos_y, color):

    queue = deque([(pos_x, pos_y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not check[ny][nx] and grid[ny][nx] == color:
                queue.append((nx, ny))
                check[ny][nx] = 1
    
    cnt[color] += 1


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(str, input().rstrip())))

check = [[0 for _ in range(n)] for _ in range(n)]
cnt = {'R': 0, 'G': 0, 'B': 0}

for color in ['R', 'G', 'B']:
    for i in range(n): 
        for j in range(n):
            if grid[i][j] == color and not check[i][j]:
                bfs(j, i, color)

t = sum(cnt.values())

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G': grid[i][j] = 'R'

cnt = {'R': 0, 'G': 0, 'B': 0}
check = [[0 for _ in range(n)] for _ in range(n)]
for color in ['R', 'B']:
    for i in range(n): 
        for j in range(n):
            if grid[i][j] == color and not check[i][j]:
                bfs(j, i, color)

print(t, sum(cnt.values()), sep = ' ')