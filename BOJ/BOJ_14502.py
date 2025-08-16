import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
# [BOJ] 14502 연구소 / 구현, 브루트포스, 그래프 이론, 그래프 탐색, BFS, 격자 그래프
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def BFS(pr, pc):
    global n, m
    visited = [[0 for _ in range(m)] for __ in range(n)]
    visited[pr][pc] = 1
    queue = deque([(pr, pc)])

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and (copiedmp[nr][nc] == 0):
                queue.append((nr, nc))
                visited[nr][nc] = 1
                copiedmp[nr][nc] = 2

def getZero():
    global n, m

    ret = 0
    for i in range(n):
        for j in range(m):
            if copiedmp[i][j] == 0:
                ret += 1
    return ret

n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]

temp = []
for i in range(n):
    for j in range(m):
        if mp[i][j] == 0:
            temp.append((i, j))

possible = list(combinations(temp, 3))
mx = -1
for k in range(len(possible)):
    visited = [[0 for _ in range(m)] for __ in range(n)]
    copiedmp = [temp[:] for temp in mp]

    for wr, wc in possible[k]:
        copiedmp[wr][wc] = 1
    
    for i in range(n):
        for j in range(m):
            if copiedmp[i][j] == 2 and not visited[i][j]:
                BFS(i, j)
    
    mx = max(mx, getZero())

print(mx)