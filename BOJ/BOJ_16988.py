import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
# [BOJ] 16988 Baaaaaaaaaduk2 (Easy) / 브루트포스, 그래프 이론, 그래프 탐색, DFS, BFS
def BFS(pr, pc):
    global n, m
    visited[pr][pc] = 1
    queue = deque([(pr, pc)])

    dr = [0, -1, 0, 1]
    dc = [-1, 0, 1, 0]
    size = 1
    flag = False
    while queue:
        qr, qc = queue.popleft()
        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if boards[nr][nc] == 0:
                    # 여기서 -1로 return 하게 되면 그룹 하나가 제대로 탐색되지 않아서 다시 탐색하게 됨.
                    # 다시 탐색하다 2를 만나면 size를 반환하게 됨
                    flag = True 
                elif boards[nr][nc] == 2:
                    size += 1
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
    
    return size if not flag else -1

n, m = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(n)]

empty = []
for r in range(n):
    for c in range(m):
        if not boards[r][c]:
            empty.append((r, c))

mx = 0
for pair in combinations(empty, 2):
    for pos in pair:
        boards[pos[0]][pos[1]] = 1

    check = 0
    visited = [[0 for __ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if boards[r][c] == 2 and not visited[r][c]:
                temp = BFS(r, c)
                if temp != -1:
                    check += temp

    for pos in pair:
        boards[pos[0]][pos[1]] = 0
    
    mx = max(check, mx)
print(mx)