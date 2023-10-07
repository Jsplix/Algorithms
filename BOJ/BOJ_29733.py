from collections import deque
import sys
input = sys.stdin.readline
# [BOJ] 29733 3차원 지뢰찾기 / 구현
r, c, h = map(int, input().split())
bomb = [[list(input().rstrip()) for _ in range(r)] for _ in range(h)]

for k in range(h):
    for j in range(r):
        for i in range(c):
            if bomb[k][j][i] == '*': continue
            else:
                bomb_cnt = 0
                for z in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        for x in [-1, 0, 1]:
                            if z == 0 and y == 0 and x == 0: continue
                            nz = k + z
                            ny = j + y
                            nx = i + x
                            if (0 <= nz < h and 0 <= ny < r and 0 <= nx < c) and (bomb[nz][ny][nx] == '*'):
                                bomb_cnt += 1
                bomb[k][j][i] = str(bomb_cnt % 10)

for c in range(h):
    for b in range(r):
        print(*bomb[c][b], sep='')