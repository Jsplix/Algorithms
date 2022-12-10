import sys
input = sys.stdin.readline
# [BOJ] 2442 별 찍기 - 5 / 구현
n = int(input())
for i in range(n):
    for j in range((n - 1) - i, 0, -1):
        print(" ", end = '')
    for k in range(2 * i + 1):
        print("*", end = '')
    print("")
