import sys
input = sys.stdin.readline
# [BOJ] 20833 Kuber / 수학, 구현, 사칙연산
sm = 0
for i in range(1, int(input()) + 1):
    sm += (i ** 3)
print(sm)