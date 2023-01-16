import sys
input = sys.stdin.readline
# [BOJ] 2446 별 찍기 9 / 구현
n = int(input())

for j in range(n-1, 0, -1):
    print(" "*(n-1-j), end='*'*(2*j+1))
    print()
for j in range(n):
    print(" "*(n-1-j) ,end='*'*(2*j+1))
    print()