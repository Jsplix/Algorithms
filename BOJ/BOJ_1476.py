import sys
import math
input = sys.stdin.readline
lcm = math.lcm
# [BOJ] 1476 날짜 계산 / 수학, 브루트 포스, 정수론
e, s, m = map(int, input().split())
x, y, z, t = 0, 0, 0, 0
while x != e or y != s or z != m:
    x += 1
    y += 1
    z += 1
    t += 1
    if x > 15:
        x = 1
    if y > 28:
        y = 1
    if z > 19:
        z = 1

print(t)