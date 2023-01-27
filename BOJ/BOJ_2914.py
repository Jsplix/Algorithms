import sys
input = sys.stdin.readline
# [BOJ] 2914 저작권 / 수학, 구현
a, b = map(int, input().split())
print(a * (b - 1) + 1)