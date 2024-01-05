import sys
input = sys.stdin.readline
# [BOJ] 7579 앱 / DP, 배낭 문제, Knapsack(냅색)
n, m = map(int, input().split())
a_arr = [0] + list(map(int, input().split())) # 용량
m_arr = [0] + list(map(int, input().split())) # 비용

mnCost = sum(m_arr)
dp = [[0 for _ in range(sum(m_arr)+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(sum(m_arr)+1):
        if j < m_arr[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - m_arr[i]] + a_arr[i])

        if dp[i][j] >= m:
            mnCost = min(mnCost, j)

print(mnCost)