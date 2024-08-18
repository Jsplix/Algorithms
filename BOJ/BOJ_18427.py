import sys
input = sys.stdin.readline
# [BOJ] 18427 함께 블록 쌓기 / DP, 배낭 문제, Knapsack
n, m, h = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] + [0 for i in range(h)]]

for i in range(n):
    dp.append(dp[i].copy())
    for b in heights[i]:
        for j in range(b, h+1):
            dp[i+1][j] += dp[i][j-b]

print(dp[n][h] % 10007)