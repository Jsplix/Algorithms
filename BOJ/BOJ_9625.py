import sys
input = sys.stdin.readline
# [BOJ] 9625 BABBA / DP
n = int(input())
dp = [[0, 0] for _ in range(46)]
dp[1][1] = 1 # dp[i][j] -> i - 버튼 누른 횟수 / j - 0이면 A의 수, 1이면 B의 수
dp[2] = [1, 1]

for i in range(3, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

print(dp[n][0], dp[n][1])