import sys
input = sys.stdin.readline
# [BOJ] 2578 빙고 / 구현, 시뮬레이션
def row_check():
    cnt = 0
    for i in range(5):
        if board[i] == ['O', 'O', 'O', 'O', 'O']: cnt += 1
    return cnt

def col_check():
    cnt = 0
    for i in range(5):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == 'O': cnt += 1
    return cnt

def diagonal_check():
    cnt = 0
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == 'O': cnt += 1
    if board[4][0] == board[3][1] == board[2][2] == board[1][3] == board[0][4] == 'O': cnt += 1
    return cnt

board = [list(map(int, input().split())) for _ in range(5)]
call_num = [list(map(int, input().split())) for _ in range(5)]

r_idx, c_idx = 0, 0
check = 0
i, j = 0, 0
while True:
    check = 0
    if board[i][j] == call_num[r_idx][c_idx]:
        c_idx += 1
        board[i][j] = 'O'
        check += row_check()
        check += col_check()
        check += diagonal_check()
    i += 1
    if i == 5: j += 1; i = 0
    if j == 5: i, j = 0, 0
    if c_idx == 5: r_idx += 1; c_idx = 0
    
    if check >= 3: break

print(5*r_idx + c_idx)