import sys
input = sys.stdin.readline
# [BOJ] 11312 삼각 무늬 - 2 / 수학, 사칙연산
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a**2 // b**2)