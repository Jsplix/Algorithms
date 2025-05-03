import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2933 미네랄 / 구현, 그래프 이론, 그래프 탐색, 시뮬레이션, BFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# --
def fall(cluster, visited):
    for pr, pc in cluster:
        cave[pr][pc] = '.'
    
    a = 0
    flag = False
    while True:
        a += 1
        for pr, pc in cluster:
            if pr + a >= r or cave[pr+a][pc] == 'x': 
                flag = True 
                break

        if flag: break
    
    for pr, pc in cluster:
        cave[pr+a-1][pc] = 'x'
        visited[pr+a-1][pc] = 1

# -- 
def throw(h, direction): # left side => direction: True / right side => direction: False
    global r, c
    for col in range(0 if direction else c-1, c if direction else -1, 1 if direction else -1):
        if cave[h][col] == 'x':
            cave[h][col] = '.'
            return True # return True : shot minerals / return False : no minerals

    return False
# -- 
def BFS(y, x, visited):
    global r, c
    queue = deque([(y, x)])
    visited[y][x] = 1

    ret = [(y, x)] # return cluster : list
    while queue:
        qy, qx = queue.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and cave[ny][nx] == 'x':
                queue.append((ny, nx))
                visited[ny][nx] = 1
                ret.append((ny, nx))

    return ret
# --
def cluster_search():
    global r, c

    visited = [[0 for _ in range(c)] for __ in range(r)]
    for col in range(c):
        if not visited[r-1][col] and cave[r-1][col] == 'x':
            BFS(r-1, col, visited)
    
    for row in range(r-1):
        for col in range(c):
            if not visited[row][col] and cave[row][col] == 'x':
                cluster = BFS(row, col, visited)
                fall(cluster, visited)

r, c = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))

for i in range(n):
    h = r - heights[i]
    if throw(h, True if i % 2 == 0 else False):
        cluster_search()

for row in range(r):
    print(*cave[row], sep='')