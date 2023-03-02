import sys
input = sys.stdin.readline
# [BOJ] 1343 폴리오미노 / 구현, 그리디
board = input().rstrip()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board: print(-1)
else: print(board)