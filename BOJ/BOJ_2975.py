import sys
input = sys.stdin.readline
# [BOJ] 2975 Transactions / 수학, 구현, 사칙연산
while True:
    info = list(input().split())
    if info[0] == '0' and info[1] == 'W' and info[2] == '0': break

    a, b = int(info[0]), int(info[2])
    if info[1] == 'W':
        if a - b < -200: print("Not allowed")
        else: print(a - b)
    elif info[1] == 'D':
        print(a + b)