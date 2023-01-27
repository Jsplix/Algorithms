import sys
input = sys.stdin.readline
# [BOJ] 1247 부호 / 수학
for _ in range(3):
    num = []
    for _ in range(int(input())):
        num.append(int(input()))
    if sum(num) == 0:
        print(0)
    elif sum(num) > 0:
        print('+')
    else:
        print('-')