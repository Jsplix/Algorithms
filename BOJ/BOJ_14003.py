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
        chk[idx[i]] = arr[i]

print(len(chk) - 1)

max_idx = max(idx) + 1
ans = []
for i in range(n, -1, -1):
    if idx[i] == max_idx - 1:
        ans.append(arr[i])
        max_idx = idx[i]
print(*ans[::-1])