import sys
input = sys.stdin.readline
# [BOJ] 12738 가장 긴 증가하는 부분 수열 3 / 이분 탐색, 가장 긴 증가하는 부분 수열(LIS)
def lowerBound(dp, target):
    left, right = 0, len(dp)

    while left < right:
        mid = (left + right) // 2

        if dp[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

N = int(input())
arr = list(map(int, input().split()))

dp = []

for num in arr:
    pos = lowerBound(dp, num)

    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))
