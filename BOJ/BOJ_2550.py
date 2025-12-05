import sys
input = sys.stdin.readline
# [BOJ] 2550 전구 / DP, 가장 긴 증가하는 부분 수열(LIS)
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
L = list(map(int, input().split()))
R = list(map(int, input().split()))

pairs = [[L[i], R[i]] for i in range(N)]

records = [0 for _ in range(N)]
dp = []
for i in range(N):
    num = R.index(pairs[i][0])

    pos = binarySearch(num)
    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num
    
    records[i] = pos

t = len(dp) - 1
result = []
for i in range(N - 1, -1, -1):
    if records[i] == t:
        result.append(pairs[i][0])
        t -= 1

result.sort()
print(len(dp))
print(*result)