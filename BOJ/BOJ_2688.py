import sys
input = sys.stdin.readline
# [BOJ] 2688 줄어들지 않아 / DP
t = int(input())

dp = [ [0 for _ in range(10)] for _ in range(65) ]
for i in range(10):
    dp[1][i] = 1

for _ in range(t):
    n = int(input())
    for i in range(2, n + 1):
        dp[i][0] = sum(dp[i - 1])
        for j in range(1, 10):
            dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]
    print(sum(dp[n]))