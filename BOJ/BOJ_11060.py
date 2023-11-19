import sys
input = sys.stdin.readline
# [BOJ] 11060 점프 점프 / DP, 그래프 이론, 그래프 탐색, BFS
MX = 1004
n = int(input())
maze = list(map(int, input().split()))

dp = [MX for _ in range(n)]
dp[0] = 0

for i in range(n):
    for j in range(1, maze[i]+1):
        if i + j >= n: 
            break
        dp[i+j] = min(dp[i] + 1, dp[i+j])

if dp[-1] == MX: print(-1)
else: print(dp[-1])