import sys
input = sys.stdin.readline
# [BOJ] 17175 피보나치는 지겨웡~ / DP
MOD = 10**9 + 7
n = int(input())
dp = [1, 1] + [0 for _ in range(n)]
for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % MOD
print(dp[n])