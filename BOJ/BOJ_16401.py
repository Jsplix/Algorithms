import sys
input = sys.stdin.readline
# [BOJ] 16401 과자 나눠주기 / 이분 탐색
m, n = map(int, input().split())
snack_len = list(map(int, input().split()))

start = 1
end = int(1e9)+1
ans = 0

while start <= end:
    chk = 0
    mid = (start + end) // 2

    for x in snack_len:
        chk += (x // mid)
    
    if chk >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)