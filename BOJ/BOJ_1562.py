import sys
input = sys.stdin.readline

# [BOJ] 1562 계단 수 / 비트마스킹, DP, 비트필드 DP

MOD = 1000000000
n = int(input())
# dp[자릿수][비트마스킹]
dp = [[0 for _ in range(1<<10)] for _ in range(10)]
for i in range(1, 10):
    dp[i][1<<i] = 1

for _ in range(2, n+1):
    next_dp = [[0 for _ in range(1<<10)] for _ in range(10)]
    for i in range(10):
        for j in range(1<<10):
            if i > 0: next_dp[i][j | (1<<i)] = (next_dp[i][j | (1<<i)] + dp[i-1][j]) % MOD
            if i < 9: next_dp[i][j | (1<<i)] = (next_dp[i][j | (1<<i)] + dp[i+1][j]) % MOD
    dp = next_dp

print(sum(dp[i][1023] for i in range(10))%MOD)