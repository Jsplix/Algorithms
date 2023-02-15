import sys
input = sys.stdin.readline
# [BOJ] 4883 삼각 그래프 / DP
k = 1
while True:
    n = int(input())
    if n == 0: break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dp = [[0, 0, 0] for _ in range(n)]
    dp[1][0] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][1]+graph[0][2])
    dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1]+graph[0][2])

    for i in range(2, n):
        for j in range(3):
            if j == 0: dp[i][j] = graph[i][j] + min(dp[i-1][j], dp[i-1][j+1])
            elif j == 1: dp[i][j] = graph[i][j] + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
            else: dp[i][j] = graph[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    print('%d. %d' %(k, dp[n-1][1]))
    k += 1