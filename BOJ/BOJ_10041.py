import sys
input = sys.stdin.readline
# [BOJ] 10041 관광 / 수학, 사칙연산, 많은 조건 분기
w, h, n = map(int, input().split())
x, y = map(int, input().split())
mn = 0
for _ in range(n-1):
    nx, ny = map(int, input().split())
    cx, cy = nx-x, ny-y

    if cx > 0 and cy > 0:
        mn += max(cx, cy)
    elif cx < 0 and cy < 0:
        mn += abs(min(cx, cy))
    else:
        mn += abs(cx) + abs(cy)
    
    x, y = nx, ny

print(mn)