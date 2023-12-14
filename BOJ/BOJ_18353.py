import sys
input = sys.stdin.readline
# [BOJ] 18353 병사 배치하기 / DP, 가장 긴 증가하는 부분 수열(LIS)
n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
# 가장 긴 감소하는 부분 수열의 길이를 구해서 총 수열의 길이에서 빼줌 -> 가장 긴 증가하는 부분 수열 삭제
for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# 이후 길이의 차를 통해서 최소 횟수를 구한다.
print(n-max(dp))