import sys
input = sys.stdin.readline
# [BOJ] 7862 틱택토 / 구현, 백트래킹
def valid_check(board, case):
    if board[0] == case and board[0] == board[1] == board[2]: return True
    elif board[0] == case and board[0] == board[3] == board[6]: return True
    elif board[4] == case and board[3] == board[4] == board[5]: return True
    elif board[4] == case and board[1] == board[4] == board[7]: return True
    elif board[8] == case and board[2] == board[5] == board[8]: return True
    elif board[8] == case and board[6] == board[7] == board[8]: return True
    elif board[0] == case and board[0] == board[4] == board[8]: return True
    elif board[2] == case and board[2] == board[4] == board[6]: return True
    else: return False

while True:
    game = input().rstrip()
    if game == 'end': break
    x_cnt = game.count('X')
    o_cnt = game.count('O')

    if x_cnt == o_cnt+1 or x_cnt == o_cnt:
        case_1, case_2 = ('X', 'O') if x_cnt == o_cnt+1 else ('O', 'X')
        res_1 = valid_check(game, case_1)
        res_2 = valid_check(game, case_2)

        if res_2: print('invalid')
        elif not res_1:
            if game.count('.') == 0: print('valid')
            else: print('invalid')
        else: print('valid')
    else: print('invalid')