import sys
input = sys.stdin.readline
# [BOJ] 2212 센서 / 그리디, 정렬
n = int(input())
k = int(input())
arr = sorted(list(map(int, input().split())))

if n <= k: print(0)
else:
    gap = []
    for i in range(1, n):
        gap.append(arr[i]-arr[i-1])

    gap.sort()
    for i in range(k-1):
        gap.pop()
    print(sum(gap))