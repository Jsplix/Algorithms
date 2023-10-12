import sys
input = sys.stdin.readline
# [BOJ] 21317 징검다리 건너기 / DP
n = int(input())
egy = [(5001, 5001)] + [tuple(map(int, input().split())) for _ in range(n-1)]
k = int(input())

dp = [[0 for _ in range(n+1)] for _ in range(2)]
for i in range(2, n+1):
    dp[0][i] = min(dp[0][i-1] + egy[i-1][0], dp[0][i-2] + egy[i-2][1])
    dp[1][i] = min(dp[1][i-1] + egy[i-1][0], dp[1][i-2] + egy[i-2][1])
    if i >= 4:
        dp[1][i] = min(dp[1][i], dp[0][i-3] + k)

print(min(dp[0][n], dp[1][n]))