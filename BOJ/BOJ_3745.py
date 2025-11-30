import sys
input = sys.stdin.readline
# [BOJ] 3745 오름세 / 이분 탐색, 가장 긴 증가하는 부분 수열(LIS)
def binarySearch(target):
    left, right = 0, len(dp)
    while left < right:
        mid = (left + right) // 2
        if dp[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

while True:
    try:
        N = int(input())
        p = list(map(int, input().split()))

        dp = []
        for num in p:
            pos = binarySearch(num)

            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        
        print(len(dp))
    except:
        break