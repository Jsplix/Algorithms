import sys
input = sys.stdin.readline
# [BOJ] 1358 하키 / 기하학
w, h, x, y, p = map(int, input().split())
mn_x, mx_x = x - h // 2, x + w + h // 2

radius = h // 2
count = 0
for _ in range(p):
    tx, ty = map(int, input().split())

    if x <= tx <= x + w and y <= ty <= y + h: count += 1
    else:
        l = ((x-tx) ** 2 + ((y+radius)-ty) ** 2) ** 0.5
        r = (((x+w)-tx) ** 2 + ((y+radius)-ty) ** 2) ** 0.5
            
        if radius >= l or radius >= r: count += 1
print(count)