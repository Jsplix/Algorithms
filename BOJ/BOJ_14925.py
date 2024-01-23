import sys
input = sys.stdin.readline
# [BOJ] 14925 목장 건설하기 / DP
m, n = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(m)]
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

mx = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if not lands[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            mx = max(mx, dp[i][j])

print(mx)