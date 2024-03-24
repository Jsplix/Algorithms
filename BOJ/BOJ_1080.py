import sys
input = sys.stdin.readline
# [BOJ] 1080 행렬 / 그리디
def convert(row, col):
    for r in range(row, row+3):
        for c in range(col, col+3):
            init[r][c] ^= 1

n, m = map(int, input().split())
init = [list(map(int, input().rstrip())) for _ in range(n)]
target = [list(map(int, input().rstrip())) for _ in range(n)]

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if init[i][j] != target[i][j]:
            convert(i, j)
            cnt += 1

if init == target: print(cnt)
else: print(-1)