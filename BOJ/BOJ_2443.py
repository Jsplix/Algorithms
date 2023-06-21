import sys
input = sys.stdin.readline
# [BOJ] 2443 별 찍기 - 6 / 구현
n = int(input())
for i in range(n, -1, -1):
    for j in range(n-i):
        print(" ", end='')
    print('*'*(2*i-1))