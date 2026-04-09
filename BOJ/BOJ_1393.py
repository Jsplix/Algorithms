import sys
input = sys.stdin.readline
# [BOJ] 1393 음하철도 구구팔 / 수학, 브루트포스, 정수론
def get_distance(x1, y1):
    global xs, ys
    return ((x1 - xs) ** 2 + (y1 - ys) ** 2) ** 0.5

# 점과 직선 사이의 최단 거리를 구하는 문제
xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())

mn = 10004
mx, my = 0, 0
if dx == 0 and dy != 0:
    for y in range(ye, 101 if dy >= 0 else -101, 1 if dy >= 0 else -1):
        dist = get_distance(xe, y)

        if dist < mn:
            mx, my = xe, y
            mn = dist
    
    print(mx, my)
elif dx != 0 and dy == 0:
    for x in range(xe, 101 if dx >= 0 else -101, 1 if dx >= 0 else -1):
        dist = get_distance(x, ye)

        if dist < mn:
            mx, my = x, ye
            mn = dist

    print(mx, my)
elif dx == 0 and dy == 0:
    print(xe, ye)
else:
    for i in range(xe, 101 if dx > 0 else -101, 1 if dx > 0 else -1):
        y = ((dy * (i - xe)) / dx) + ye
        dist = get_distance(i, y)

        if dist < mn:
            mx, my = i, int(y)
            mn = dist

    print(mx, my)