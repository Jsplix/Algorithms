import sys
input = sys.stdin.readline

def check(n, board):
    res = 0
    for i in range(n):
        cnt_w = 1
        cnt_l = 1
        for j in range(1, n):
            for k in range(j, j + 1):
                if board[i][k] == board[i][k - 1]: # 색이 같으면 cnt값 + 1
                    cnt_w += 1
                else: # 색이 다르면 cnt값 0으로 초기화
                    cnt_w = 1
                if board[k][i] == board[k - 1][i]:
                    cnt_l += 1
                else:
                    cnt_l = 1
            res = max(res, cnt_w, cnt_l)
    return res

n = int(input())
board = []
for i in range(n):
    board.append(list(map(str, input().rstrip())))

cnt = []
cnt.append(check(n, board))

if max(cnt) == n:
    print(n)
else:
    for i in range(n):
        for j in range(1, n):
            for k in range(j, j + 1):
                if board[i][k] != board[i][k - 1]:
                    board[i][k], board[i][k - 1] = board[i][k - 1], board[i][k] # 인접한 것과 다르면 바꿔주기
                    cnt.append(check(n, board))
                    board[i][k], board[i][k - 1] = board[i][k - 1], board[i][k] # 다시 원래대로 돌려주기
                if board[k][i] != board[k - 1][i]:
                    board[k][i], board[k - 1][i] = board[k - 1][i], board[k][i]
                    cnt.append(check(n, board))
                    board[k][i], board[k - 1][i] = board[k - 1][i], board[k][i]
    print(max(cnt))                    