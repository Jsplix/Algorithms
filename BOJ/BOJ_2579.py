import sys
input = sys.stdin.readline
# [BOJ] 2579 계단 오르기 / DP
n = int(input())
step = [0]
for _ in range(n):
    step.append(int(input()))

dp = [ [0 for _ in range(3)] for _ in range(n + 1) ]
if n == 1:
    print(step[1])
    exit(0)
dp[1][1], dp[2][1] = step[1], step[2]
dp[1][2], dp[2][2] = 0, step[1] + step[2]

for i in range(3, n + 1):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + step[i]
    dp[i][2] = dp[i - 1][1] + step[i]

print(max(dp[n][1], dp[n][2]))