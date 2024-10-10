import sys
input = sys.stdin.readline
# [BOJ] 12026 BOJ 거리 / DP
MX = 10**9 + 7
n = int(input())
blocks = list(input().rstrip())
dp = [MX for _ in range(n)]

dp[0] = 0
for i in range(n):
    for j in range(i+1, n):
        if dp[i] == -1: 
            dp[j] = -1
            continue

        if blocks[i] == 'B' and blocks[j] == 'O':
            dp[j] = min(dp[i] + (j-i)**2, dp[j])

        if blocks[i] == 'O' and blocks[j] == 'J':
            dp[j] = min(dp[i] + (j-i)**2, dp[j])

        if blocks[i] == 'J' and blocks[j] == 'B':
            dp[j] = min(dp[i] + (j-i)**2, dp[j])
    
if dp[n-1] == MX: print(-1)
else: print(dp[n-1])