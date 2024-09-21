import sys
input = sys.stdin.readline
# [BOJ] 32209 다음 달에 봐요 / 수학, 구현, 사칙연산
p = 0
flag = False
for _ in range(int(input())):
    x, y = map(int, input().split())

    if flag: continue
    if x == 1:
        p += y
    elif x == 2:
        if p < y: flag = True
        else: p -= y

if flag: print("Adios")
else: print("See you next month")