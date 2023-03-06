import sys
input = sys.stdin.readline
# [20551] Sort 마스터 배지훈의 후계자 / 이분 탐색, 정렬, 자료 구조
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

for i in range(m):
    d = int(input())
    flag = False
    answer = int(1e9)
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < d:
            start = mid + 1
        elif arr[mid] == d:
            answer = min(answer, mid)
            flag = True
            end = mid - 1
        else:
            end = mid - 1
    if flag: print(answer)
    else: print(-1)