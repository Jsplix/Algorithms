import sys
input = sys.stdin.readline
# [BOJ] 13711 LCS 4 / 가장 긴 증가하는 부분 수열(LIS), 최장 공통 부분 수열(LCS)
def binarySearch(target):
    left, right = 0, len(dp)
    while left < right:
        mid = (left + right) // 2

        if dp[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

index = {i: -1 for i in range(1, N + 1)}
for i in range(N):
    index[A[i]] = i

dp = []
for i in range(N):
    num = index[B[i]]
    pos = binarySearch(num)

    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

print(len(dp))