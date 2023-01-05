import sys
input = sys.stdin.readline
# [BOJ] 2229 조 짜기 / DP
n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(n):
    dp[i + 1] = dp[i]
    minValue = maxValue = arr[i]
    j = i - 1
    while j >= 0 and (arr[j] < minValue or arr[j] > maxValue):
        minValue = min(arr[j], minValue)
        maxValue = max(arr[j], maxValue)
        dp[i + 1] = max(dp[i + 1], dp[j] + maxValue - minValue)
        j -= 1

print(dp[n])