import sys
input = sys.stdin.readline
# [BOJ] 20500 Ezreal 여눈부터 가네 ㅈㅈ / 수학, DP, 정수론
# DFS로 dp값을 찾아보니 아래의 점화식과 같은 규칙을 발견할 수 있었음.
# 직관으로 풀었다면 못 풀었을 수도 있을듯함.
MOD = 1000000007
n = int(input())
dp = [0, 0, 1, 1, 3, 5, 11]
for i in range(7, 1516):
    dp.append((2*dp[i-2] + dp[i-1]) % MOD)
print(dp[n])