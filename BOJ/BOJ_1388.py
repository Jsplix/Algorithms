import sys
input = sys.stdin.readline
# [BOJ] 1388 바닥 장식 / 구현, 그래프 이론, 그래프 탐색, DFS
def check_col(c_size, r, c):
    visited[r][c] = 1
    for i in range(c + 1, c_size):
        if floor[r][i] == '|':
            return 1
        else:
            visited[r][i] = 1
    return 1
        
def check_row(r_size, r, c):
    visited[r][c] = 1
    for i in range(r + 1, r_size):
        if floor[i][c] == '-':
            return 1
        else:
            visited[i][c] = 1
    return 1


n, m = map(int, input().split())
floor = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

board = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if floor[i][j] == '|':
                board += check_row(n, i, j)
            if floor[i][j] == '-':
                board += check_col(m, i, j)

print(board)