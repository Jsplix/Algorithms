import sys
input = sys.stdin.readline
# [BOJ] 25916 싫은데요 / 투 포인터
n, m = map(int, input().split())
arr = list(map(int, input().split()))

if n == 1:
    if arr[0] <= m: print(arr[0])
    else: print(0)
else:
    l, r = 0, 1
    now, answer = arr[l], 0
    while l <= r and r < n:
        if now + arr[r] <= m:
            now += arr[r]
            r += 1
        else:
            if l == r:
                l += 1
                r += 1
                now = 0
                continue
            now -= arr[l]
            l += 1
        answer = max(answer, now)
    print(answer)