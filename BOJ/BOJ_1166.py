import sys
input = sys.stdin.readline
# [BOJ] 1166 선물 / 이분 탐색
n, l, w, h = map(int, input().split())
mn, mx = 0, min(l, w, h)

for _ in range(100):
    mid = (mn + mx) / 2
    if (l//mid)*(w//mid)*(h//mid) >= n:
        mn = mid
    else:
        mx = mid

print(mx)