import sys
input = sys.stdin.readline
# [BOJ] 14494 다이나믹이 뭐예요? / DP
MOD = 10**9 + 7
dp = [[0 for _ in range(1001)] for _ in range(1001)]
n, m = map(int, input().split())
dp[0][0] = 1

for i in range(1, 1001):
    for j in range(1, 1001):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j-1] + dp[i-1][j]) % MOD

print(dp[n][m])