import sys
input = sys.stdin.readline
# [BOJ] 15482 한글 LCS / DP, 문자열, 파싱, LCS, utf-8 입력 처리
A = [''] + list(input().rstrip())
B = [''] + list(input().rstrip())

dp = [['' for _ in range(len(B))] for __ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + B[j]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[-1][-1]))