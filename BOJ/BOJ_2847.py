import sys
input = sys.stdin.readline
# [BOJ] 2847 게임을 만든 동준이 / 그리디
n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n-1, 0, -1):
    if arr[i] <= arr[i-1]:
        cnt += (arr[i-1]-arr[i]) + 1
        arr[i-1] -= (arr[i-1]-arr[i]) + 1
print(cnt)