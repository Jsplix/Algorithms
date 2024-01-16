import sys
input = sys.stdin.readline
# [BOJ] 2248 이진수 찾기 / DP
N, L, I = map(int, input().split())
dp = [[1 for _ in range(31) ] + [0]] + [[0 for _ in range(32)] for _ in range(31)]

for i in range(1, N+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

answer = ''
for b in range(N, 0, -1):
    if I <= dp[b-1][L]:
        answer += '0'
    else:
        answer += '1'
        I -= dp[b-1][L]
        L -= 1
print(answer)