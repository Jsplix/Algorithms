from math import cos, radians, sin, sqrt, tan
import sys
input = sys.stdin.readline
# [BOJ] 2936 채식주의사 / 기하, 구현
x, y = map(int, input().split())

if (x != 0 and y == 0) or (x == 0 and y == 0):
    if x == 250:
        m = 0
        n = 125
    else:
        if x > 125:
            l = (125 * 250) / x
            m = 0
            n = l
        else:
            l = (125 * 250) / ((250 - x) * sin(radians(45)))
            m = 250 - (l * cos(radians(45)))
            n = l * sin(radians(45))
elif x == 0 and y != 0:
    if y == 250:
        m = 125
        n = 0
    else:
        if y > 125:
            l = (125 * 250) / y
            m = l
            n = 0
        else:
            l = (125 * 250) / ((250 - y) * sin(radians(45)))
            m = l * sin(radians(45))
            n = 250 - (l * cos(radians(45)))
else:
    if x != 0 and y != 0 and x > 125 and y < 125:
        l = sqrt(x**2 + (250-y)**2)
        k = (125 * 250) / (l * sin(radians(45)))
        m = 0
        n = 250 - k
    else:
        l = sqrt((250-x)**2 + y**2)
        k = (125 * 250) / (l * sin(radians(45)))
        m = 250 - k
        n = 0

print('{0:.2f} {1:.2f}'.format(abs(m), abs(n)))