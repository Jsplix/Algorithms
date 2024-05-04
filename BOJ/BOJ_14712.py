import sys
input = sys.stdin.readline
# [BOJ] 14712 넴모넴모 (Easy) / 브루트포스, 백트래킹
def back(r, c):
    global answer
    if (r, c) == (n, 0):
        answer += 1
        return

    if c == m-1:
        nr, nc = r + 1, 0
    else:
        nr, nc = r, c + 1
    
    back(nr, nc)

    if not board[r][c-1] or not board[r-1][c] or not board[r-1][c-1]:
        board[r][c] = 1
        back(nr, nc)
        board[r][c] = 0

n, m = map(int, input().split())
board = [[0 for _ in range(m)] for __ in range(n)]
answer = 0

back(0, 0)
print(answer)