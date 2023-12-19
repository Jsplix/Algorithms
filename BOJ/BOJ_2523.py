import sys
input = sys.stdin.readline
# [BOJ] 2523 별 찍기 - 13 / 구현
n = int(input())
for i in range(1, n+1):
    print('*'*i)
for j in range(n-1, 0, -1):
    print('*'*j)