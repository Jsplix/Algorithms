import sys
input = sys.stdin.readline
# [BOJ] 13702 이상한 술집 / 이분 탐색
n, k = map(int, input().split())
drink = sorted(list(int(input()) for _ in range(n)))

left, right = 0, drink[-1]
total = sum(drink)

answer = drink[0]
while left <= right:
    mid = (left + right) // 2

    chk = 0
    if mid == 0: break
    for d in drink:
        chk += (d//mid)
    
    if k <= chk:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)