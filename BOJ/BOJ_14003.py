from bisect import bisect_left
import sys
input = sys.stdin.readline
# [BOJ] 14003 가장 긴 증가하는 부분 수열 5 / 이분 탐색
MI_INF = int(-1e9) - 1

n = int(input())
arr = list(map(int, input().split()))
chk = [MI_INF]
idx = [0 for _ in range(n + 1)]

for i in range(n):
    if chk[-1] < arr[i]:
        chk.append(arr[i])
        idx[i] = len(chk) - 1
    else:
        idx[i] = bisect_left(chk, arr[i])
        # bisect는 정렬된 배열(리스트)에서 이분 탐색을 진행힘.
        # left는 해당 배열에서 값보다 작거나 같은 가장 큰 index를 반환하고
        # right는 해당 배열에서 값보다 크거나 같은 가장 작은 index를 반환한다.
        chk[idx[i]] = arr[i]

print(len(chk) - 1)
# print(chk)

max_idx = max(idx) + 1
ans = []
for i in range(n, -1, -1):
    if idx[i] == max_idx - 1:
        ans.append(arr[i])
        max_idx = idx[i]
print(*ans[::-1])