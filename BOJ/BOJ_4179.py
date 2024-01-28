import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 4179 불! / 그래프 이론, 그래프 탐색, BFS
r, c = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(r)]

queue = deque([])
visited = [[0 for _ in range(c)] for _ in range(r)]
move = {}
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J': queue.appendleft((j, i, 'J', 1)) ; move[(j, i)] = 1 ; visited[i][j] = 1
        elif maze[i][j] == 'F': queue.append((j, i, 'F', -1)) ; visited[i][j] = 1

chk = []
def bfs():

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y, w, cnt = queue.popleft()
        if w == 'J' and not move[(x, y)]: maze[y][x] = 'F' ; w = 'F'
        if w == 'J' and (x == 0 or x == c-1 or y == 0 or y == r-1) and move[(x, y)]: chk.append(cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if visited[ny][nx]:
                    if w == 'J':
                        if maze[ny][nx] == 'F': continue
                    elif w == 'F':
                        if maze[ny][nx] == 'J': move[(nx, ny)] = 0 ; continue 
                elif not visited[ny][nx] and maze[ny][nx] != '#':
                    if w == 'J': 
                        queue.append((nx, ny, w, cnt + 1))
                        move[(nx, ny)] = 1
                    elif w == 'F': 
                        queue.append((nx, ny, w, cnt))

                    visited[ny][nx] = 1
                    if w == 'J': maze[y][x], maze[ny][nx] = maze[ny][nx], w
                    elif w == 'F': maze[ny][nx] = 'F'
        move[(x, y)] = 0

bfs()
if chk: print(min(chk))
else: print("IMPOSSIBLE")