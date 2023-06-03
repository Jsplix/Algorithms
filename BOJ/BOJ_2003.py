import sys
input = sys.stdin.readline
# [BOJ] 2003 수들의 합 2 / 브루트 포스, 누적 합, 투 포인터
n, m = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 1
cnt = 0
while r <= n and l <= r: 
    chk = sum(arr[l:r])
    if chk == m:
        cnt += 1
        r += 1
    elif chk < m:
        r += 1
    else:
        l += 1
print(cnt)