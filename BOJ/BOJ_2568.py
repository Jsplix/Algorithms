import sys
input = sys.stdin.readline
# [BOJ] 2568 전깃줄 - 2 / 역추적, 가장 긴 증가하는 부분 수열 문제(LIS)
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
pairs = [list(map(int, input().split())) for _ in range(N)]

pairs.sort()

dp = []
record = [0 for _ in range(N)]
for i in range(N):
    num = pairs[i][1]
    pos = binarySearch(num)

    if pos == len(dp):
        dp.append(num)
    else:
        dp[pos] = num

    record[i] = pos

last = len(dp) - 1
result = [0 for _ in range(N)]
for i in range(N - 1, -1, -1):
    if record[i] == last:
        result[i] = 1
        last -= 1

    if last < 0: break

print(N - len(dp))
for i in range(N):
    if not result[i]:
        print(pairs[i][0])
