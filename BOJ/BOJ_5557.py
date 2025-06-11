import sys
input = sys.stdin.readline
# [BOJ] 5557 1학년 / DP
n = int(input())
arr = list(map(int, input().split()))
result = 0

dp = [[0 for _ in range(21)] for __ in range(n-1)]
dp[0][arr[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        if j-arr[i] >= 0:
            dp[i][j-arr[i]] += dp[i-1][j]
        if j+arr[i] <= 20:
            dp[i][j+arr[i]] += dp[i-1][j]

print(dp[-1][arr[-1]])