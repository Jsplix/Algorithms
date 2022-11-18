import sys
input = sys.stdin.readline
# [BOJ] 9461 파도반 수열 - DP
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        if i == 2:
            dp[i] = 1
            continue
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[n])