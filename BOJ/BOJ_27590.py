import sys
input = sys.stdin.readline
# [BOJ] 27590 Sun and Moon / 구현, 브루트포스, 시뮬레이션
a, b = map(int, input().split())
c, d = map(int, input().split())

y = 0
while True:
    if (y + a) % b == 0 and (y + c) % d == 0:
        print(y)
        break
    y += 1