import sys
input = sys.stdin.readline
# [BOJ] 13250 주사위 게임 / DP, 수학, 확률론
N = int(input())

dp = [0 for _ in range(10**6 + 7)]
dp[1] = 1
dp[2] += dp[1] / 6 + 1
dp[3] += (dp[1] + dp[2]) / 6 + 1
dp[4] += (dp[1] + dp[2] + dp[3]) / 6 + 1
dp[5] += (dp[1] + dp[2] + dp[3] + dp[4]) / 6 + 1
dp[6] += (dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) / 6 + 1

for i in range(7, N + 1):
    dp[i] += (dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4] + dp[i - 5] + dp[i - 6]) / 6 + 1

print(dp[N])