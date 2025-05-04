import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 18500 미네랄 2 / 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, BFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def throw(h, k):
    global r, c
    s, e = 0 if k == 1 else c-1, c if k == 1 else -1
    for col in range(s, e, k):
        if cave[h][col] == 'x':
            cave[h][col] = '.'
            return col
    
    return -1

def fall(coordinations):
    global r, c

    for tr, tc in coordinations:
        cave[tr][tc] = '.'
    
    flag, t = True, 0
    while flag:
        t += 1
        for tr, tc in coordinations:
            if tr + t >= r or cave[tr+t][tc] == 'x':
                flag = False
                break
    
    for tr, tc in coordinations:
        cave[tr+t-1][tc] = 'x'

def check():
    global r, c
    visited = [[0 for _ in range(c)] for __ in range(r)]
    cluster = []

    for i in range(c):
        if not visited[-1][i] and cave[-1][i] == 'x':
            BFS(r-1, i, visited)

    for i in range(r-1):
        for j in range(c):
            if not visited[i][j] and cave[i][j] == 'x':
                cluster = BFS(i, j, visited)
                break

        if cluster:
            break

    if cluster:
        fall(cluster)

    
def BFS(y, x, visited):
    global r, c
    queue = deque([(y, x)])
    visited[y][x] = 1

    locations = [(y, x)]
    while queue:
        qy, qx = queue.popleft()
        for i in range(4):
            ny = qy + dy[i]
            nx = qx + dx[i]
            if 0 <= ny < r and 0 <= nx < c and cave[ny][nx] == 'x' and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = 1
                locations.append((ny, nx))

    return locations

r, c = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))

for i in range(n):
    h = r - heights[i]
    k = -1 if i % 2 else 1
    p = throw(h, k)
    if p != -1:
        check()

for i in range(r):
    print(*cave[i], sep='')