import sys
input = sys.stdin.readline
# [BOJ] 5582 공통 부분 문자열 / DP, 문자열, 최장 공통 부분 수열 문제
s = input().rstrip()
t = input().rstrip()

dp = [[0 for _ in range(len(t) + 1)] for __ in range(len(s) + 1)]
mx = 0
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            mx = max(mx, dp[i][j])

print(mx)