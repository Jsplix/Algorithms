import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
# [BOJ] 2533 사회망 서비스(SNS) / DP, 트리, 트리DP
def dfs(node):
    dp[node][1] = 1 
    visited[node] = 1

    for next in graph[node]:
        if not visited[next]:
            dfs(next)
            dp[node][0] += dp[next][1]
            dp[node][1] += min(dp[next][0], dp[next][1])

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]

dfs(1)

print(min(dp[1]))