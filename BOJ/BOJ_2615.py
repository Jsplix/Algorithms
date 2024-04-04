import sys
input = sys.stdin.readline
# [BOJ] 2615 오목 / 구현, 브루트포스
board = [list(map(int, input().split())) for _ in range(19)]
dr = [0, -1, 1, 1]
dc = [1, 1, 0, 1]

def check(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        cnt = 1

        while 0 <= nr < 19 and nc < 19 and board[nr][nc] == board[r][c]:
            cnt += 1
            nr += dr[i]
            nc += dc[i]
            if cnt == 5:
                if not (0<=nr<19 and 0<=nc<19 and board[nr][nc] == board[r][c]):
                    if not (0<=r-dr[i]<19 and 0<=c-dc[i]<19 and board[r-dr[i]][c-dc[i]] == board[r][c]):
                        print(board[r][c])
                        print(r+1, c+1)
                        exit(0)
                    else:
                        break
                else:
                    break

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            check(i, j)

print(0)