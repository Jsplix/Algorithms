import sys
input = sys.stdin.readline
# [BOJ] 15966 군계일학 / DP
n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(10**6+1)]
for i in range(n):
    x = arr[i]
    dp[x] = max(dp[x], dp[x-1] + 1)

print(max(dp))