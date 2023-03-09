import sys
input = sys.stdin.readline
# [BOJ] 2167 2차원 배열의 합 / 구현, 누적 합
n, m = map(int, input().split())
mtrx = [[*map(int, input().split())] for _ in range(n)]
total = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        total[i][j] = total[i-1][j] + total[i][j-1] - total[i-1][j-1] + mtrx[i-1][j-1]

for k in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    print(total[r2][c2]-total[r2][c1-1]-total[r1-1][c2]+total[r1-1][c1-1])