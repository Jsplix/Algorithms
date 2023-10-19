import sys
input = sys.stdin.readline
# [BOJ] 17390 이건 꼭 풀어야 해! / 정렬, 누적 합
n, q = map(int, input().split())
arr = [0] + sorted(list(map(int, input().split())))
for i in range(1, n+1):
    arr[i] += arr[i-1]

for _ in range(q):
    l, r = map(int, input().split())
    if l == r: print(arr[r]-arr[l-1])
    else: print(arr[r]-arr[l-1])