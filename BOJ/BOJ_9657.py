import sys
input = sys.stdin.readline
# [BOJ] 9657 돌 게임 3 / DP, 게임 이론
n = int(input())
dp = [0 for _ in range(1001)] # 1 - SK, 0 - CY

dp[1], dp[3], dp[4] = 1, 1, 1
if n >= 5:
    for i in range(5, n+1):
        if not dp[i-1]: dp[i] = 1
        if not dp[i-3]: dp[i] = 1
        if not dp[i-4]: dp[i] = 1

if dp[n]: print("SK")
else: print("CY")