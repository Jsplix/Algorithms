import sys
input = sys.stdin.readline
# [BOJ] 16493 최대 페이지 수 / DP, 브루트포스, 냅색(Knapsack), 배낭 문제, 백트래킹
n, m = map(int, input().split())
reading = [tuple(map(int, input().split())) for _ in range(m)]

dp = [0 for _ in range(n + 1)]
for i in range(m):
    for j in range(n, -1, -1):
        if j - reading[i][0] >= 0:
            dp[j] = max(dp[j], dp[j-reading[i][0]] + reading[i][1])
print(dp[n])