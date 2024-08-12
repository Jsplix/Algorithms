import sys
input = sys.stdin.readline
# [BOJ] 1757 달려달려 / DP
n, m = map(int, input().split())
d = [0] + [int(input()) for _ in range(n)]

dp = [[0 for _ in range(m+1)] for __ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j-1] + d[i]
        dp[i][0] = max(dp[i][0], dp[i-j][j])

print(dp[-1][0])