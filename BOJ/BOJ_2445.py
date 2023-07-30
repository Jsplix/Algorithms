import sys
input = sys.stdin.readline
# [BOJ] 2445 별 찍기 - 8 / 구현
n = int(input())
for i in range(1, n+1):
    for j_1 in range(i):
        print('*', end='')
    for k in range(2*(n-i)):
        print(" ", end='')
    for j_2 in range(i):
        print('*', end='')
    print('')
for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end='')
    for k in range(2*(n-i)):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')