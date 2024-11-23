import sys
input = sys.stdin.readline
# [BOJ] 11320 삼각 무늬 - 1 / 수학, 사칙연산
for _ in range(int(input())):
    a, b = map(int, input().split())
    answer = a**2 // b**2
    print(answer)