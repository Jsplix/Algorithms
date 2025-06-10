import sys
input = sys.stdin.readline
# [BOJ] 1965 상자넣기 / DP
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)] # dp[i] -> i번째 상자까지 한번에 넣을 수 있는 최대 상자 개수

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))