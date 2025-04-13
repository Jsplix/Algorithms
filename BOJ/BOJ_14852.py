import sys
input = sys.stdin.readline
# [BOJ] 14852 타일 채우기 3 / DP
n = int(input())
dp = [1, 2, 7]
MOD = 10**9 + 7
for i in range(3, n+1):
    dp.append((3*dp[i-1] + dp[i-2] - dp[i-3]) % MOD)
print(dp[n])