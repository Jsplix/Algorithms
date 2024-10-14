import sys
input = sys.stdin.readline
# [BOJ] 2304 창고 다각형 / 구현, 자료 구조, 브루트포스, 스택
n = int(input())
roofs = [list(map(int, input().split())) for _ in range(n)]
roofs.sort(key=lambda x:(x[0]))

mx_height, mx_idx = 0, 0
h = [0 for _ in range(1001)]
for i in range(n):
    pos, height = roofs[i] 
    h[pos] = height
    if mx_height <= height:
        mx_height = height
        mx_idx = pos

total = 0
now = 0
for i in range(mx_idx+1):
    now = max(h[i], now)
    total += now

now = 0
for i in range(1000, mx_idx, -1):
    now = max(h[i], now)
    total += now

print(total)