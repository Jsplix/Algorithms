import sys
input = sys.stdin.readline
# [BOJ] 14650 걷다보니 신천역 삼 (Small) / 수학, DP, 정수론, 브루트 포스
n = int(input())
dp = [0 for _ in range(10)]
dp[2] = 2
for i in range(3, 10):
    dp[i] = 3*dp[i-1]
print(dp[n])
# itertools 모듈의 product를 이용하니 자릿수가 늘어날때마다 이전 자릿수의 3배가 됨을 확인