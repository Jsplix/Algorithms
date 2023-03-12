import sys
input = sys.stdin.readline
# [BOJ] 3009 네번째 점 / 구현, 기하학
x, y = [], []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
rx, ry = 0, 0
for i in range(3):
    if x.count(x[i]) == 1:
        rx = x[i]
    if y.count(y[i]) == 1:
        ry = y[i]

print(rx, ry)
