import sys
input = sys.stdin.readline
# [BOJ] 11051 이항 계수 2 / DP
n, r = map(int, input().split())
c = [ [0 for _ in range(1001)] for _ in range(n + 1) ]
for i in range(n + 1): # c[n][r]
    c[i][0] = 1
    for j in range(i + 1):
        if j == i:
            c[i][j] = 1
        else:
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
print(c[n][r] % 10007)