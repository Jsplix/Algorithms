import sys
input = sys.stdin.readline
# [BOJ] 17206 준석이의 수학 숙제 / 수학, 포함 배제의 원리
n = int(input())
case = list(map(int, input().split()))

dp = [0 for _ in range(100001)]
for i in range(1, 100001):
    if i % 3 == 0: dp[i] = dp[i-1] + i
    elif i % 7 == 0: dp[i] = dp[i-1] + i
    else: dp[i] = dp[i-1]

for t in case:
    print(dp[t])