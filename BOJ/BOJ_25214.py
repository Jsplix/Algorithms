import sys
input = sys.stdin.readline
# [BOJ] 25214 크림 파스타 / DP, 그리디
n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]
mn = arr[0]

for i in range(1, n):
    mn = min(arr[i], mn)
    dp[i] = max(dp[i-1], arr[i]-mn)

print(*dp)