import sys
input = sys.stdin.readline
# [BOJ] 27968 사사의 사차원 사탕 봉지 / 누적 합, 이분 탐색
n, m = map(int, input().split())
pop_cnt = list(map(int, input().split()))
accum = [0 for _ in range(m)]
for i in range(m):
    accum[i] += pop_cnt[i] + accum[i-1]

for i in range(n):
    k = int(input())
    answer = 300006
    left, right = 0, m-1
    if k > accum[-1]: print("Go away!")
    else:
        while left <= right:
            mid = (left + right) // 2
            if accum[mid] >= k:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        print(answer + 1)