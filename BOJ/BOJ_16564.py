import sys
input = sys.stdin.readline
# [BOJ] 16564 히오스 프로게이머 / 이분 탐색
n, k = map(int, input().split())
x = [ int(input()) for _ in range(n) ]
x.sort()

start = x[0]
end = x[-1] + k
chk = []

while start <= end:
    mid = (start + end) // 2
    
    total = 0
    for level in x:
        if mid > level:
            total += mid - level

    if total <= k:
        start = mid + 1
        chk.append(mid)
    else:
        end = mid - 1

print(max(chk))