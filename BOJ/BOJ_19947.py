import sys
input = sys.stdin.readline
# [BOJ] 19947 투자의 귀재 배주형 / DP, 브루트 포스
h, y = map(int, input().split())
# 복리기 때문에 그리디 X -> DP로 해결해야함.
dp = [h] + [0 for _ in range(11)]

for i in range(1, 11):
    if i >= 5:
        dp[i] = max(dp[i-1]*1.05, dp[i-3]*1.20, dp[i-5]*1.35)
    elif i >= 3:
        dp[i] = max(dp[i-1]*1.05, dp[i-3]*1.20)
    else:
        dp[i] = dp[i-1]*1.05
    dp[i] = int(dp[i])

print(dp[y])