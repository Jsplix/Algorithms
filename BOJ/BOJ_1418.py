import sys
input = sys.stdin.readline
# [BOJ] 1418 K-세준수 / 수학, 에라토스테네스의 체, 브루트포스
n = int(input())
k = int(input())

arr = [0 for _ in range(n + 1)]

for i in range(2, n+1):
    if arr[i]: continue
    for j in range(i, n+1, i):
        arr[j] = max(arr[j], i)

cnt = 0
for i in range(1, n+1):
    if arr[i] <= k:
        cnt += 1

print(cnt)