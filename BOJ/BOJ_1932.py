import sys
input = sys.stdin.readline
# [BOJ] 1932 정수 삼각형 / DP
n = int(input())
dp = [0]
for i in range(n):
    dp.append(list(map(int, input().split())))

if n > 1:
    dp[2][0] += dp[1][0]
    dp[2][1] += dp[1][0]

for i in range(2, n):
    for j in range(len(dp[i]) + 1):
        if j != 0 and j != len(dp[i]):
            dp[i + 1][j] += max(dp[i][j - 1:j + 1])
        if j == 0:
            dp[i + 1][j] += dp[i][j]
        if j == len(dp[i]):
            dp[i + 1][j] += dp[i][j - 1]

print(max(dp[n]))