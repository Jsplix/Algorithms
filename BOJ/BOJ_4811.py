import sys
input = sys.stdin.readline
# [BOJ] 4811 알약 / DP
dp = [[0 for _ in range(31)] for _ in range(31)]
for i in range(31):
    for j in range(31):
        if i > j: continue
        if i == 0: dp[j][i] = 1
        else: dp[j][i] = dp[j-1][i] + dp[j][i-1]

for _ in range(1000):
    n = int(input())
    if n == 0: break
    print(dp[n][n])