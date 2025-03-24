import sys
input = sys.stdin.readline
# [BOJ] Hunt The Rabbit / 구현, 이분 탐색
while True:
    n = int(input())
    if not n: break

    left, right = 1, 50
    hist = []
    while left <= right:
        mid = (left + right) // 2
        hist.append(mid)
        if n == mid: 
            print(*hist)
            break
        elif n < mid:
            right = mid-1
        else:
            left = mid+1