import sys
input = sys.stdin.readline
# [BOJ] 14500 테트로미노 / 구현, 브루트 포스
# pypy3 로 제출 + 브루트 포스로 풀어보기
# 골드 구현 문제
n, m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
visit = [ ([0] * m) for _ in range(n) ]

max_sum = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num, summ):
    global n, m, board, dx, dy, max_sum
    if num == 4:
        max_sum = max(max_sum, summ)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if not visit[nx][ny]:
            visit[nx][ny] = 1
            dfs(nx, ny, num + 1, summ + board[nx][ny])
            visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visit[i][j] = 0

        # ㅏ , ㅗ , ㅓ, ㅜ 모양 검사
        # ㅏ
        if i < n - 2 and j < m - 1:
            max_sum = max(max_sum, board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])
        # ㅜ
        if i < n - 1 and j < m - 2:
            max_sum = max(max_sum, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1])
        # ㅗ
        if i >= 1 and j < m - 2:
            max_sum = max(max_sum, board[i][j] + board[i][j + 1] + board[i - 1][j + 1] + board[i][j + 2])
        # ㅓ
        if 1 <= i < n - 1 and j < m - 1:
            max_sum = max(max_sum, board[i][j] + board[i][j + 1] + board[i - 1][j + 1] + board[i + 1][j + 1])

print(max_sum)