import sys
input = sys.stdin.readline
# [BOJ] 11568 민균이의 계략 / DP, LIS
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))