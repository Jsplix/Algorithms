import sys
input = sys.stdin.readline
# [BOJ] 27159 노 땡스! / 구현
n = int(input())
arr = list(map(int, input().split()))

sm = arr[0]
for i in range(1, n):
    if arr[i-1] + 1 != arr[i]: sm += arr[i]
print(sm)