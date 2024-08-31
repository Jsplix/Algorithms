import sys
input = sys.stdin.readline
# [BOJ] 13301 타일 장식물 / 수학, DP
n = int(input())
dp = [0 for _ in range(81)]
l = [0 for _ in range(81)] # 한 변의 길이

dp[1], dp[2] = 4, 6
l[1], l[2] = 1, 1
for i in range(3, 81):
    l[i] = l[i-1] + l[i-2]
    dp[i] = (dp[i-1] - l[i] + (3 * l[i]))

print(dp[n])