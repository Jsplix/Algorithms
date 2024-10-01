import sys
input = sys.stdin.readline
# [BOJ] 28353 고양이 카페 / 그리디, 정렬, 투 포인터
n, k = map(int, input().split())
weights = sorted(map(int, input().split()))

answer = 0
l, r = 0, n-1
while l < r and r < n:
    if weights[l] + weights[r] <= k:
        l += 1
        r -= 1
        answer += 1
    else:
        r -= 1
print(answer)