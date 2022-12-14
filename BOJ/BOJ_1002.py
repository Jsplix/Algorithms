from math import sqrt
import sys
input = sys.stdin.readline

# [BOJ] 1002 터렛 / 수학, 기하

test_case = int(input())
for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue

    r = x1**2 - x2**2 + y1**2 - y2**2 - r1**2  + r2**2
    a = -2 * x1 + 2 * x2
    b = -2 * y1 + 2 * y2
    dist_1 = abs(a * x1 + b * y1 + r) / sqrt(a**2 + b**2)
    dist_2 = abs(a * x2 + b * y2 + r) / sqrt(a**2 + b**2)

    if dist_1 < r1 and dist_2 < r2:
        print(2)
    elif dist_1 == r1 and dist_2 == r2:
        print(1)
    elif dist_1 > r1 or dist_2 > r2:
        print(0)