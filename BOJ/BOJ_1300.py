import sys
input = sys.stdin.readline
# [BOJ] 1300 k번째 수 / 이분 탐색, 매개 변수 탐색
n = int(input())
k = int(input())

start = 0
end = k

while start <= end:
    mid = (start + end) // 2
    chk = 0
    for i in range(1, n + 1): # 오름차순 정렬이므로 1부터 해줌
        chk += min(mid // i, n) # 1부터 n까지 각 수들이 몇개씩 있는지 (k전까지) 확인
    
    if chk >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)