import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2589 보물섬 / 그래프 이론, 그래프 탐색, BFS, 격자 그래프, 브루트포스 
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def bfs(pr, pc):
    global l, w, mx
    visited = [[0 for _ in range(w)] for __ in range(l)]
    
    queue = deque([(pr, pc, 0)])
    visited[pr][pc] = 1

    ret = 0
    while queue:
        r, c, cnt = queue.popleft()
        mx = max(mx, cnt)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            while 0 <= nr < l and 0 <= nc < w and mp[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, cnt+1))

l, w = map(int, input().split())
mp = [list(input().rstrip()) for _ in range(l)]

mx = 0
for i in range(l):
    for j in range(w):
        if mp[i][j] == 'L':
            bfs(i, j)

print(mx)