import sys
input = sys.stdin.readline
# [BOJ] 24523 내 뒤에 나와 다른 수 / 구현, 자료 구조
n = int(input())
arr = list(map(int, input().split()))
result = [-1 for _ in range(n)]

l, r = 0, 1
while l <= r and r < n:
    if arr[l] == arr[r]:
        r += 1
    else:
        for i in range(l, r):
            result[i] = (r+1)
        l = r
        r += 1
print(*result)