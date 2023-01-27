import sys
input = sys.stdin.readline
# [BOJ] 16401 과자 나눠주기 / 이분 탐색
m, n = map(int, input().split())
snack_len = list(map(int, input().split()))

start = 0
end = max(snack_len)
ans = 0

# 이분탐색을 통해서 어떤 길이로 과자를 나눠줄지 결정
while start <= end: 
    chk = 0
    mid = (start + end) // 2
    if mid == 0:
        ans = 0
        break

    for x in snack_len:
        if x >= mid:
            chk += (x // mid)
    
    if chk >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)