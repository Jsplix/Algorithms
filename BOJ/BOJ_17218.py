import sys
input = sys.stdin.readline
# [BOJ] 17218 비밀번호 만들기 / DP, 문자열, 역추적, LCS
A = [''] + list(input().rstrip())
B = [''] + list(input().rstrip())

la, lb = len(A), len(B)
dp = [['' for _ in range(lb)] for __ in range(la)]

for i in range(la):
    for j in range(lb):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + B[j]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(dp[-1][-1])