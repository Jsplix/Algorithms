import sys
input = sys.stdin.readline
# [BOJ] 10599 페르시아의 왕들 / 수학, 구현, 사칙연산
while True:
    info = list(map(int, input().split()))
    if info == [0, 0, 0, 0]: break

    mn, mx = info[2] - info[1], info[3] - info[0]
    print(mn, mx)