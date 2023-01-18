import sys
input = sys.stdin.readline
# [BOJ] 1699 제곱수의 합 / DP, 브루트 포스
N = int(input())
dp = [i for i in range(N + 1)]

for i in range(N + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1

print(dp[N])