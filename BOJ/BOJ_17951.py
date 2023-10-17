import sys
input = sys.stdin.readline
# [BOJ] 17951 흩날리는 시험지 속에서 내 평점이 느껴진거야 / 이분 탐색, 매개 변수 탐색
n, k = map(int, input().split())
sol = list(map(int, input().split()))

left, right = 0, int(2e6)+1
mn = 0
while left <= right:
    mid = (left + right) // 2
    total, group = 0, 0
    for p in sol:
        total += p
        if total >= mid:
            group += 1
            total = 0
    
    if group >= k:
        mn = mid
        left = mid + 1
    else:
        right = mid - 1

print(mn)