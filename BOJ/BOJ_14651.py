import sys
input = sys.stdin.readline
# [BOJ] 14651 걷다보니 신천역 삼 (Large) / DP, 수학, 정수론
MOD = 10**9 + 9

n = int(input())
dp = [0 for _ in range(33334)]
dp[2], dp[3] = 2, 6

# 0, 1, 2로 이루어진 N자리 수에서 3의 배수의 개수 -> N-1자리의 3의 배수 개수 * 3
for i in range(4, n+1):
    dp[i] = (dp[i-1] * 3) % MOD

print(dp[n])