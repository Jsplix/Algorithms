import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
# [BOJ] 욕심쟁이 판다 / DP, 그래프 이론, 그래프 탐색, DFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(px, py, bamboo, depth):
    global n, mx

    if mp[(py, px)]: return mp[(py, px)]

    for i in range(4):
        nx = px + dx[i]
        ny = py + dy[i]

        if 0 <= ny < n and 0 <= nx < n and forest[ny][nx] > bamboo:
            mp[(py, px)] = max(mp[(py, px)], dfs(nx, ny, forest[ny][nx], depth + 1) + 1)

    return 1 if not mp[(py, px)] else mp[(py, px)]

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

mp = defaultdict(int)
for i in range(n):
    for j in range(n):
        if not mp[(i, j)]:
            mp[(i, j)] = dfs(j, i, forest[i][j], 1)
        
print(max(mp.values()))