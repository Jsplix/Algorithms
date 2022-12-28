import sys
input = sys.stdin.readline
# [BOJ] 2110 공유기 설치 / 이분 탐색(Binary Search), 매개 변수 탐색(Parametric Search)
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[n - 1] - arr[0]
dist = []

while start <= end:
    mid = (start + end) // 2 # mid는 공유기 사이의 거리를 나타냄
    now = arr[0] # now -> 공유기 설치 할 집의 위치
    cnt = 1

    for i in range(n):
        if arr[i] >= now + mid:
            cnt += 1
            now = arr[i]
    
    if cnt >= m:
        start = mid + 1
        dist.append(mid)
    else:
        end = mid - 1

print(max(dist)) # 공유기 사이의 거리들 중 최대를 출력