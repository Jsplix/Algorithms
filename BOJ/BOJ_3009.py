import sys
input = sys.stdin.readline

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
