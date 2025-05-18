import sys
input = sys.stdin.readline
# [BOJ] 18398 HOMWRK / 수학, 구현, 사칙연산
for _ in range(int(input())):
    for __ in range(int(input())):
        a, b = map(int, input().split())
        print(a+b, a*b)