import sys
input = sys.stdin.readline
# [BOJ] 1964 오각형, 오각형, 오각형… / 수학
# n단계에서는 n-1 단계의 점 개수 + 2*(n+1) + (n-1)
n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 5
for i in range(2, n+1):
    dp[i] = (dp[i-1] + 2*(i+1) + (i-1)) % 45678
print(dp[n])