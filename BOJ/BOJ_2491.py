import sys
input = sys.stdin.readline
# [BOJ] 2491 수열 / 구현, DP
N = int(input())
arr = list(map(int, input().split()))

mx = [1 for _ in range(N)]
mn = [1 for _ in range(N)]

for i in range(N - 1):
    if arr[i] <= arr[i + 1]:
        mx[i + 1] = mx[i] + 1
    if arr[i] >= arr[i + 1]:
        mn[i + 1] = mn[i] + 1

print(max(max(mn), max(mx)))