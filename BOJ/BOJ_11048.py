import sys
input = sys.stdin.readline
# [BOJ] 11048 이동하기 / DP
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = maze[i-1][j-1] + max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
print(dp[n][m])