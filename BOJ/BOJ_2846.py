import sys
input = sys.stdin.readline
# [BOJ] 2846 오르막길 / 구현
n = int(input())
arr = list(map(int, input().split()))

i, j = 0, 1
result = 0
while i <= j and j < n:
    if arr[i] < arr[j] and arr[j-1] < arr[j]:
        j += 1
    else:
        result = max(result, arr[j-1] - arr[i])
        i = j
        j += 1

result = max(result, arr[j-1] - arr[i])     
print(result)