import sys
from collections import deque
input = sys.stdin.readline
# [BOJ] 2823 유턴 싫어 / 그래프 이론, BFS, DFS
def bfs(pr, pc):
    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    
    queue = deque([(pr, pc)])
    visited[pr][pc] = 1

    while queue:
        qr, qc = queue.popleft()
        temp = 0
        for i in range(4):
            nr, nc = qr + dr[i], qc+ dc[i]
            if 0 <= nr < r and 0 <= nc < c and villages[nr][nc] == '.':
                temp += 1
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
        
        if temp < 2:
            return 0
    
    return 1

r, c = map(int, input().split())
villages = [list(input().rstrip()) for _ in range(r)]


visited = [[0 for _ in range(c)] for __ in range(r)]    
for i in range(r):
    for j in range(c):
        if villages[i][j] == '.':
            print(bfs(i, j)^1)
            exit(0)
