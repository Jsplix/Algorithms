import sys
input = sys.stdin.readline
# [BOJ] 2210 숫자왕 점프 / 그래프 이론, 그래프 탐색, 브루트 포스, DFS
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(nx, ny, num: str):
    num += board[ny][nx]
    if len(num) == 6:
        if num not in chk:
            chk.append(num)
        return

    for i in range(4):
        x = nx + dx[i]
        y = ny + dy[i]
        if 0 <= x < 5 and 0 <= y < 5:
            dfs(x, y, num)

chk = []
board = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(chk))