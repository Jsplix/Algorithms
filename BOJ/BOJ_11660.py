import sys
input = sys.stdin.readline
# [BOJ] 11660 구간 합 구하기 5 / DP, 누적 합
n, m = map(int, input().split())
mtrx = [list(map(int, input().split())) for _ in range(n)]

accum_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        accum_sum[i][j] = accum_sum[i-1][j] + accum_sum[i][j-1] - accum_sum[i-1][j-1] + mtrx[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = accum_sum[x2][y2] - accum_sum[x2][y1-1] - accum_sum[x1-1][y2] + accum_sum[x1-1][y1-1]
    print(answer)