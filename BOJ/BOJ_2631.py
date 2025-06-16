import sys
input = sys.stdin.readline
# [BOJ] 2631 줄세우기 / DP
n = int(input())
seq = [0] + [int(input()) for _ in range(n)]

dp = [1 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))