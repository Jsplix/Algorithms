import sys
input = sys.stdin.readline
# [BOJ] 2428 표절 / 정렬, 이분 탐색
n = int(input())
files = sorted(map(int, input().split()))

answer = 0
for i in range(n):
    left, right = i, n
    while left < right:
        mid = (left + right) // 2
        if files[i] >= files[mid] * 0.9:
            left = mid + 1
        else:
            right = mid
    
    answer += (right - i - 1)
print(answer)