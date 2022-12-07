import sys
input = sys.stdin.readline
# [BOJ] 12865 평범한 배낭 / DP, Knapsack
n, k = map(int, input().split())
w, v = [0], [0]
dp = [ [0 for _ in range(k + 1)] for _ in range(n + 1) ] 
# dp[i] - 순서 / dp[i][j] - i번째까지의 가방 무게 (가치가 최대가 되는)

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < w[i]: # j는 현재 가방 용량
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
# 이전 배낭, 추가할 물건의 무게만큼 빼주고 현재 물건 추가 중 가치가 더 높은 것을 선택
# 현재 추가할 물건의 무게를 뺄 때, 해당 무게가 없는 것에 대해서는 이미 해당 무게가 없을때의 최대 가치가
# dp배열에 저장되어 있기 때문에 신경쓰지 않아도 됨
print(dp[n][k])