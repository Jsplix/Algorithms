import sys
input = sys.stdin.readline
# [BOJ] 14659 한조서열정리하고옴ㅋㅋ / 그리디
n = int(input())
height = list(map(int, input().split()))

if n == 1: print(0)
else:
    i, j = 0, 1
    h = 0
    mx = -1
    while i <= j and j < n:
        if height[i] > height[j]: 
            h += 1
            j += 1
        else:
            mx = max(mx, h)
            i = j
            j = i + 1
            h = 0
            continue
    mx = max(h, mx)
    print(mx)