import sys
input = sys.stdin.readline
# [BOJ] 23827 수열 (Easy) / 수학, 누적 합
MOD = 10**9 + 7

n = int(input())
arr = list(map(int, input().split()))
accum_sum = [0 for _ in range(n)]

accum_sum[0] = arr[0]
for i in range(1, n):
    accum_sum[i] = accum_sum[i-1] + arr[i]

result = 0
for i in range(n):
    result += arr[i] * (accum_sum[-1] - accum_sum[i])
    result %= MOD
print(result)