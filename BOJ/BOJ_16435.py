import sys
input = sys.stdin.readline
# [BOJ] 16435 스네이크버드 / 그리디, 정렬
n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))
for i in range(n):
    if h[i] <= l:
        l += 1
print(l)
