import sys
input = sys.stdin.readline
# [BOJ] 15989 1, 2, 3 더하기 4 / DP
dp = [0, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14]
for i in range(11, 10001):
    dp.append(dp[i-3] + (i//2) + 1)

for _ in range(int(input())):
    n = int(input())
    print(dp[n])