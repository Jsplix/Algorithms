import sys
input = sys.stdin.readline
# [BOJ] 13240 Chessboard / 구현
n, m = map(int, input().split())
for r in range(n):
    for c in range(m):
        if (r + c) % 2: print('.', end='')
        else: print('*', end='')
    print()