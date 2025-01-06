import sys
input = sys.stdin.readline
# [BOJ] 2705 팰린드롬 파티션 / DP, 재귀
dp = [0 for _ in range(1001)]
dp[1] = 1
for i in range(2, 1001):
    if i % 2: dp[i] = dp[i-1]
    else: dp[i] = dp[i // 2] + dp[i - 1]

for _ in range(int(input())):
    print(dp[int(input())])