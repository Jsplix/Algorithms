import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 6593 상범 빌딩 / 그래프 이론, 그래프 탐색, BFS
def bfs(pos_x, pos_y, pos_z):
    global l, r, c
    queue = deque([(pos_x, pos_y, pos_z, 0)])
    visited = [[[0 for _ in range(c)] for __ in range(r)] for ___ in range(l)]
    visited[pos_z][pos_y][pos_x] = 1

    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while queue:
        x, y, z, cnt = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < c and 0 <= ny < r and 0 <= nz < l:
                if not visited[nz][ny][nx] and buildings[nz][ny][nx] != '#':
                    if buildings[nz][ny][nx] == 'E': 
                        return ("Escaped in", cnt + 1, "minute(s).")
                    visited[nz][ny][nx] = 1
                    queue.append((nx, ny, nz, cnt + 1)) 

    return ("Trapped!", )

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0: break
    buildings = []
    for i in range(l):
        buildings.append([])
        for j in range(r):
            buildings[i].append(list(input().rstrip()))
        empty = input()
    
    flag = False
    for f in range(l):
        for i in range(r):
            for j in range(c):
                if buildings[f][i][j] == 'S':
                    print(*bfs(j, i, f))
                    flag = True
                    break
            if flag: break
        if flag: break