import sys
input = sys.stdin.readline
# [BOJ] 17212 달나라 토끼를 위한 구매대금 지불 도우미 / DP
MAX = 10**5 + 8
n = int(input())

dp = [0 for _ in range(MAX)]
for i in range(1, n+1):
    if i < 2:
        dp[i] = 1
    elif i < 5:
        dp[i] = min(dp[i-1], dp[i-2]) + 1
    elif i < 7:
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5]) + 1
    else:
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1

print(dp[n])