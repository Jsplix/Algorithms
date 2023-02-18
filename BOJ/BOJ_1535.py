import sys
input = sys.stdin.readline
# [BOJ] 1535 안녕 / DP, 브루트 포스, 냅색(Knapsack)
n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[0 for _ in range(100)] for _ in range(n+1)]
for i in range(n): # 인사한 사람 수
    for j in range(100): # 체력 대비 최대 기쁨
        if j < L[i]: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])

print(max(dp[n-1]))