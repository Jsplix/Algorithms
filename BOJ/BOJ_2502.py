import sys
input = sys.stdin.readline
# [BOJ] 2502 떡 먹는 호랑이 / 수학, DP, 브루트 포스
d, k = map(int, input().split())

arr = [0 for _ in range(d+1)]
for i in range(1, 100001):
    arr[1] = i
    for j in range(i+1, 100001):
        arr[2] = j
        if arr[1] + arr[2] > k: break
        for l in range(3, d+1):
            arr[l] = arr[l-1] + arr[l-2]
        if arr[d] == k:
            print(arr[1], arr[2], sep='\n')
            exit(0)