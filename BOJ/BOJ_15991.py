import sys
input = sys.stdin.readline
# [BOJ] 15991 1, 2, 3 더하기 6 / DP
MX = 10**5 + 7
MOD = 10**9 + 9

dp = [0 for _ in range(MX)]
dp[1], dp[2], dp[3], dp[4], dp[5], dp[6] = 1, 2, 2, 3, 3, 6

for i in range(7, 10**5 + 1):
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % MOD

for _ in range(int(input())):
    print(dp[int(input())])